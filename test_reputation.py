#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test script for the reputation system
"""

from bot_detection import ReputationSystem
import datetime
import os

def main():
    """Test the reputation system directly"""
    print(f"Current working directory: {os.getcwd()}")
    print(f"Script directory: {os.path.dirname(os.path.abspath(__file__))}")
    
    # Print the reputation file location
    from bot_detection import REPUTATION_FILE
    print(f"Reputation file location: {REPUTATION_FILE}")
    print(f"File exists: {os.path.exists(REPUTATION_FILE)}")
    
    # Create reputation system
    reputation_system = ReputationSystem()
    
    # Get user reputation
    username = "user"
    reputation = reputation_system.get_user_reputation(username)
    print(f"Initial reputation for {username}: {reputation}")
    
    # Log a report submission
    print("Logging report submission...")
    reputation_system.log_report_submission(username, is_valid=True)
    
    # Check reputation again
    reputation = reputation_system.get_user_reputation(username)
    print(f"Updated reputation for {username}: {reputation}")
    
    # Log a series of rapid reports (simulating bot behavior)
    print("Logging rapid reports (simulating bot behavior)...")
    for i in range(5):
        reputation_system.log_report_submission(username, is_valid=False)
        reputation = reputation_system.get_user_reputation(username)
        print(f"Reputation after suspicious report {i+1}: {reputation}")

if __name__ == "__main__":
    main()
