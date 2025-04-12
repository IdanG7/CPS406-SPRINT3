#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Bot Detection Module

This module provides utilities for detecting and preventing automated report
submissions by bots, as well as tracking user reputation and suspicious activity.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QSize

import os
import json
import random
import string
import datetime
import traceback

# File to store user reputation data using absolute path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPUTATION_FILE = os.path.join(SCRIPT_DIR, 'user_reputation.json')

# Global reputation system instance (singleton)
_reputation_system_instance = None

class ReputationSystem:
    """
    Manages user reputation and tracks suspicious activity.
    
    This class handles the tracking of user reputation scores and flags,
    allowing the system to identify potentially problematic users.
    """
    
    def __init__(self):
        """Initialize the reputation system."""
        self.reputation_data = {}
        self._load_reputation_data()
        print(f"ReputationSystem instance created")
    
    def _load_reputation_data(self):
        """Load reputation data from the JSON file."""
        if os.path.exists(REPUTATION_FILE):
            try:
                with open(REPUTATION_FILE, 'r') as file:
                    data = file.read().strip()
                    if data:
                        self.reputation_data = json.loads(data)
                        print(f"Successfully loaded reputation data from {REPUTATION_FILE}")
                    else:
                        print(f"Warning: Reputation file exists but is empty. Creating default.")
                        self.reputation_data = {}
                        self._save_reputation_data()
            except Exception as e:
                print(f"Error loading reputation data: {e}")
                traceback.print_exc()
                print(f"Creating new reputation data")
                self.reputation_data = {}
                self._save_reputation_data()
        else:
            print(f"Reputation file does not exist, creating default at: {REPUTATION_FILE}")
            self.reputation_data = {}
            self._save_reputation_data()
    
    def _save_reputation_data(self):
        """Save reputation data to the JSON file."""
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(REPUTATION_FILE), exist_ok=True)
            
            print(f"Saving to {REPUTATION_FILE}, data: {self.reputation_data}")
            
            # Write the data
            with open(REPUTATION_FILE, 'w') as file:
                json.dump(self.reputation_data, file, indent=4)
                file.flush()
                os.fsync(file.fileno())
            
            # Verify the data was written correctly
            if os.path.exists(REPUTATION_FILE):
                with open(REPUTATION_FILE, 'r') as verify_file:
                    verify_data = verify_file.read().strip()
                    if verify_data:
                        print(f"Successfully saved and verified reputation data")
                    else:
                        print(f"WARNING: Reputation file was saved but appears to be empty!")
            else:
                print(f"WARNING: Failed to create reputation file!")
        except Exception as e:
            print(f"Error saving reputation data: {e}")
            traceback.print_exc()
    
    def get_user_reputation(self, username):
        """
        Get the reputation score for a user.
        
        Args:
            username (str): The username to check
            
        Returns:
            dict: User reputation data including score and flags
        """
        if username not in self.reputation_data:
            # Initialize new user with default values
            self.reputation_data[username] = {
                'score': 100,  # Default score (0-100)
                'flagged': False,
                'suspicious_reports': 0,
                'total_reports': 0,
                'last_report_time': None,
                'captcha_failures': 0
            }
            self._save_reputation_data()
            
        return self.reputation_data[username]
    
    def is_user_flagged(self, username):
        """
        Check if a user is flagged as suspicious.
        
        Args:
            username (str): The username to check
            
        Returns:
            bool: True if the user is flagged, False otherwise
        """
        reputation = self.get_user_reputation(username)
        return reputation['flagged']
    
    def log_report_submission(self, username, is_valid=True):
        """
        Log a report submission for a user.
        
        Args:
            username (str): The username submitting the report
            is_valid (bool): Whether the report passed validation
            
        Returns:
            bool: True if the user can proceed, False if they're blocked
        """
        reputation = self.get_user_reputation(username)
        
        # Update report counts
        reputation['total_reports'] += 1
        
        # Check if this is a suspicious submission
        if not is_valid:
            reputation['suspicious_reports'] += 1
        
        # Check for rapid submissions (potential bot behavior)
        current_time = datetime.datetime.now().isoformat()
        if reputation['last_report_time']:
            last_time = datetime.datetime.fromisoformat(reputation['last_report_time'])
            time_diff = (datetime.datetime.now() - last_time).total_seconds()
            
            # If reports are submitted too quickly (less than 30 seconds apart)
            if time_diff < 30:
                reputation['score'] = max(0, reputation['score'] - 10)
                if reputation['score'] < 50:
                    reputation['flagged'] = True
        
        # Update last report time
        reputation['last_report_time'] = current_time
        
        # Update score based on valid/invalid submissions
        if is_valid:
            # Slowly improve score for good behavior
            reputation['score'] = min(100, reputation['score'] + 1)
        else:
            # Penalize for suspicious submissions
            reputation['score'] = max(0, reputation['score'] - 5)
        
        # Flag user if score gets too low
        if reputation['score'] < 50:
            reputation['flagged'] = True
        
        # Save updated data
        self._save_reputation_data()
        
        # Return whether the user can proceed
        return not reputation['flagged']
    
    def log_captcha_failure(self, username):
        """
        Log a CAPTCHA failure for a user.
        
        Args:
            username (str): The username that failed the CAPTCHA
            
        Returns:
            bool: True if the user can retry, False if they're blocked
        """
        reputation = self.get_user_reputation(username)
        
        # Increment failure count
        reputation['captcha_failures'] += 1
        
        # Penalize for CAPTCHA failures
        reputation['score'] = max(0, reputation['score'] - 10)
        
        # Flag user if score gets too low or too many failures
        if reputation['score'] < 50 or reputation['captcha_failures'] >= 3:
            reputation['flagged'] = True
        
        # Save updated data
        self._save_reputation_data()
        
        # Return whether the user can proceed
        return not reputation['flagged']
    
    def reset_user_flags(self, username):
        """
        Reset flags for a user (admin function).
        
        Args:
            username (str): The username to reset
        """
        if username in self.reputation_data:
            self.reputation_data[username]['flagged'] = False
            self.reputation_data[username]['score'] = 70  # Restore to a moderate score
            self.reputation_data[username]['captcha_failures'] = 0
            self._save_reputation_data()


# Function to get the singleton instance of ReputationSystem
def get_reputation_system():
    """
    Get the singleton instance of the ReputationSystem.
    
    Returns:
        ReputationSystem: The global reputation system instance
    """
    global _reputation_system_instance
    if _reputation_system_instance is None:
        _reputation_system_instance = ReputationSystem()
    return _reputation_system_instance


class CaptchaDialog(QDialog):
    """Dialog for CAPTCHA verification."""
    
    def __init__(self, parent=None):
        """Initialize the CAPTCHA dialog."""
        super().__init__(parent)
        self.setWindowTitle("Verify You're Human")
        self.setFixedSize(400, 250)
        
        # Generate CAPTCHA code
        self.captcha_code = self._generate_captcha()
        
        # Create layout
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        
        # Create CAPTCHA display
        captcha_label = QLabel("Please enter the text shown below:")
        captcha_label.setFont(QFont("Arial", 12))
        layout.addWidget(captcha_label)
        
        # Display CAPTCHA text (in a real system, this would be an image)
        self.captcha_display = QLabel(self)
        self.captcha_display.setFont(QFont("Courier", 18, QFont.Bold))
        self.captcha_display.setStyleSheet("""
            background-color: #f0f0f0;
            padding: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            letter-spacing: 5px;
        """)
        self.captcha_display.setAlignment(Qt.AlignCenter)
        self.captcha_display.setText(self.captcha_code)
        layout.addWidget(self.captcha_display)
        
        # Input field for CAPTCHA
        self.captcha_input = QLineEdit()
        self.captcha_input.setFont(QFont("Arial", 12))
        self.captcha_input.setPlaceholderText("Enter the text above")
        layout.addWidget(self.captcha_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        # Refresh button
        self.refresh_button = QPushButton("New CAPTCHA")
        self.refresh_button.clicked.connect(self._refresh_captcha)
        button_layout.addWidget(self.refresh_button)
        
        # Verify button
        self.verify_button = QPushButton("Verify")
        self.verify_button.setDefault(True)
        self.verify_button.clicked.connect(self._verify_captcha)
        button_layout.addWidget(self.verify_button)
        
        layout.addLayout(button_layout)
        
        # Apply styling
        self.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 4px;
                padding: 8px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #dcdcdc;
                border-radius: 4px;
            }
        """)
    
    def _generate_captcha(self, length=6):
        """Generate a random CAPTCHA code."""
        # In a production system, this would create an image
        # For this demo, we'll use a simple text CAPTCHA
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
    
    def _refresh_captcha(self):
        """Generate a new CAPTCHA code."""
        self.captcha_code = self._generate_captcha()
        self.captcha_display.setText(self.captcha_code)
        self.captcha_input.clear()
    
    def _verify_captcha(self):
        """Verify the entered CAPTCHA code."""
        entered_code = self.captcha_input.text().upper()
        if entered_code == self.captcha_code:
            self.accept()  # Close with success
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Incorrect CAPTCHA",
                "The entered text doesn't match. Please try again."
            )
            self._refresh_captcha()


def verify_human_user(parent_widget, username):
    """
    Verify that the user is human using a CAPTCHA.
    
    Args:
        parent_widget: The parent widget for the CAPTCHA dialog
        username (str): The username attempting verification
        
    Returns:
        bool: True if verified as human, False otherwise
    """
    # Get the singleton instance of ReputationSystem
    reputation_system = get_reputation_system()
    
    # Always show CAPTCHA for flagged users
    if reputation_system.is_user_flagged(username):
        QtWidgets.QMessageBox.warning(
            parent_widget,
            "Account Flagged",
            "Your account has been flagged for suspicious activity. "
            "Please contact an administrator."
        )
        return False
    
    # Get user reputation data
    reputation = reputation_system.get_user_reputation(username)
    
    # Show CAPTCHA randomly for high-reputation users (30% chance)
    # Always show for users with lower reputation
    should_show_captcha = (
        random.random() < 0.3 or 
        reputation['score'] < 80 or
        reputation['total_reports'] % 5 == 0  # Every 5th report
    )
    
    if should_show_captcha:
        captcha_dialog = CaptchaDialog(parent_widget)
        result = captcha_dialog.exec_()
        
        if result == QDialog.Accepted:
            return True
        else:
            # Log CAPTCHA failure
            can_retry = reputation_system.log_captcha_failure(username)
            if not can_retry:
                QtWidgets.QMessageBox.warning(
                    parent_widget,
                    "Account Flagged",
                    "Your account has been flagged for suspicious activity. "
                    "Please contact an administrator."
                )
            return False
    
    return True
