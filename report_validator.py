#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Report Validator Module

This module provides utilities for automatically validating submitted reports
to detect potentially false or spam reports based on content and patterns.
"""

import json
import os
import re
import datetime
from collections import Counter

# Import reputation system
from bot_detection import get_reputation_system

# Constants - Use absolute path for reports file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_FILE = os.path.join(SCRIPT_DIR, 'reports.json')
SUSPICIOUS_THRESHOLD = 0.7  # Threshold for suspicion (0-1)

class ReportValidator:
    """
    Validates report content to detect potentially false reports.
    
    This class analyzes report content for suspicious patterns that might
    indicate automated or spam submissions.
    """
    
    def __init__(self):
        """Initialize the report validator."""
        self.reputation_system = get_reputation_system()
        self.suspicious_keywords = [
            'test', 'testing', 'asdf', 'fake', 'spam', 'junk',
            'xyz', 'qwerty', 'lorem ipsum', 'abcdef', '12345'
        ]
        
    def validate_report(self, report_data, username):
        """
        Validate a report for suspicious content.
        
        Args:
            report_data (dict): The report data to validate
            username (str): The username of the report submitter
            
        Returns:
            tuple: (is_valid, suspicion_score, reasons)
                is_valid (bool): True if the report passes validation
                suspicion_score (float): 0-1 score indicating suspicion level
                reasons (list): List of reasons for suspicion if any
        """
        suspicion_score = 0.0
        reasons = []
        
        # Check description length
        description = report_data.get('description', '')
        if len(description.strip()) < 10:
            suspicion_score += 0.2
            reasons.append("Very short description")
        
        # Check for suspicious keywords
        if any(keyword in description.lower() for keyword in self.suspicious_keywords):
            suspicion_score += 0.4
            reasons.append("Contains suspicious keywords")
        
        # Check description and problem type consistency
        problem_type = report_data.get('type', '')
        if problem_type and len(description) > 20:
            if problem_type.lower() not in description.lower():
                # The description doesn't mention the problem type at all
                suspicion_score += 0.1
        
        # Check for multiple rapid submissions from same user
        recent_reports = self._get_recent_reports_by_user(username)
        if len(recent_reports) >= 3:  # If user has submitted 3+ reports recently
            # Check time intervals
            timestamps = [self._parse_report_time(report.get('date', '')) 
                         for report in recent_reports]
            timestamps.sort()
            
            # Check if any reports were submitted within 2 minutes of each other
            for i in range(1, len(timestamps)):
                time_diff = (timestamps[i] - timestamps[i-1]).total_seconds()
                if time_diff < 120:  # Less than 2 minutes apart
                    suspicion_score += 0.3
                    reasons.append("Multiple rapid submissions")
                    break
            
            # Check for duplicate content
            descriptions = [report.get('description', '') for report in recent_reports]
            if self._has_duplicate_content(descriptions):
                suspicion_score += 0.3
                reasons.append("Similar content to recent reports")
        
        # Determine if the report is valid based on the suspicion score
        is_valid = suspicion_score < SUSPICIOUS_THRESHOLD
        
        # If report is suspicious, update user reputation
        if not is_valid:
            self.reputation_system.log_report_submission(username, is_valid=False)
        
        return (is_valid, suspicion_score, reasons)
    
    def _get_recent_reports_by_user(self, username, hours=24):
        """
        Get recent reports submitted by a user.
        
        Args:
            username (str): The username to check
            hours (int): Number of hours back to check
            
        Returns:
            list: List of recent reports by the user
        """
        now = datetime.datetime.now()
        cutoff_time = now - datetime.timedelta(hours=hours)
        
        # Load all reports
        reports = []
        if os.path.exists(REPORTS_FILE):
            try:
                with open(REPORTS_FILE, 'r') as file:
                    reports = json.load(file)
            except:
                return []
        
        # Filter reports by username and time
        recent_reports = []
        for report in reports:
            if report.get('username') == username:
                report_time = self._parse_report_time(report.get('date', ''))
                if report_time and report_time > cutoff_time:
                    recent_reports.append(report)
        
        return recent_reports
    
    def _parse_report_time(self, time_str):
        """
        Parse a report timestamp string into a datetime object.
        
        Args:
            time_str (str): Timestamp string in format 'YYYY-MM-DD HH:MM:SS'
            
        Returns:
            datetime: Parsed datetime or None if parsing fails
        """
        try:
            return datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        except:
            return None
    
    def _has_duplicate_content(self, descriptions, similarity_threshold=0.8):
        """
        Check if a list of descriptions contains similar content.
        
        Args:
            descriptions (list): List of description strings
            similarity_threshold (float): Threshold for similarity (0-1)
            
        Returns:
            bool: True if similar content is detected
        """
        # Simple implementation - check for repeated words or phrases
        for i in range(len(descriptions)):
            for j in range(i+1, len(descriptions)):
                similarity = self._calculate_text_similarity(
                    descriptions[i], descriptions[j]
                )
                if similarity > similarity_threshold:
                    return True
        
        return False
    
    def _calculate_text_similarity(self, text1, text2):
        """
        Calculate similarity between two texts.
        
        Args:
            text1 (str): First text
            text2 (str): Second text
            
        Returns:
            float: Similarity score (0-1)
        """
        # Convert to lowercase and split into words
        words1 = set(re.findall(r'\w+', text1.lower()))
        words2 = set(re.findall(r'\w+', text2.lower()))
        
        # Handle empty texts
        if not words1 or not words2:
            return 0.0
        
        # Calculate Jaccard similarity (intersection / union)
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union)


def verify_report_legitimacy(report_data, username, parent_widget=None):
    """
    Verify the legitimacy of a report.
    
    Args:
        report_data (dict): The report data to validate
        username (str): The username of the report submitter
        parent_widget: Optional parent widget for displaying messages
        
    Returns:
        bool: True if the report is deemed legitimate
    """
    validator = ReportValidator()
    is_valid, suspicion_score, reasons = validator.validate_report(report_data, username)
    
    # If the report is suspicious, show a warning
    if not is_valid and parent_widget:
        from PyQt5.QtWidgets import QMessageBox
        
        # Format the reasons
        reason_text = "\n".join([f"- {reason}" for reason in reasons])
        
        QMessageBox.warning(
            parent_widget,
            "Suspicious Report Detected",
            f"Your report has been flagged as potentially suspicious for the following reasons:\n\n"
            f"{reason_text}\n\n"
            f"Please ensure your report is accurate and detailed. Multiple suspicious reports "
            f"may result in account restrictions."
        )
    
    return is_valid
