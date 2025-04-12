#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utility to force reset the reputation file with correct permissions
"""

import os
import json

# File to store user reputation data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPUTATION_FILE = os.path.join(SCRIPT_DIR, 'user_reputation.json')

def reset_reputation_file():
    """Reset the reputation file with default values."""
    default_data = {
        "user": {
            "score": 100,
            "flagged": False,
            "suspicious_reports": 0,
            "total_reports": 0,
            "last_report_time": None,
            "captcha_failures": 0
        },
        "admin": {
            "score": 100,
            "flagged": False,
            "suspicious_reports": 0,
            "total_reports": 0,
            "last_report_time": None,
            "captcha_failures": 0
        }
    }
    
    # Delete existing file if it exists
    try:
        if os.path.exists(REPUTATION_FILE):
            os.remove(REPUTATION_FILE)
            print(f"Deleted existing reputation file: {REPUTATION_FILE}")
    except Exception as e:
        print(f"Error deleting reputation file: {e}")
    
    # Create new file with proper permissions
    try:
        with open(REPUTATION_FILE, 'w') as f:
            json.dump(default_data, f, indent=4)
            # Force flush to disk
            f.flush()
            os.fsync(f.fileno())
        print(f"Created new reputation file: {REPUTATION_FILE}")
        print(f"File exists: {os.path.exists(REPUTATION_FILE)}")
        print(f"File permissions: {oct(os.stat(REPUTATION_FILE).st_mode)}")
        print(f"File is writable: {os.access(REPUTATION_FILE, os.W_OK)}")
    except Exception as e:
        print(f"Error creating reputation file: {e}")

if __name__ == "__main__":
    reset_reputation_file()
