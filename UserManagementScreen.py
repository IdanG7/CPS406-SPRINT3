from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox, QDialog
from PyQt5.QtWidgets import QLineEdit, QComboBox, QFormLayout, QDialogButtonBox, QCheckBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon, QPixmap, QColor

from bot_detection import get_reputation_system

import json
import os
import datetime

# Import global variables from main_ui
from main_ui import userData, active_user, isAdminUser

class Ui_UserManagementScreen(object):
    """
    UI definition for the User Management Screen.
    
    This class defines all the UI components for the user management screen,
    including the layout, widgets, and styling.
    """
    
    def setupUi(self, UserManagementScreen):
        """Set up the UI components for the User Management Screen."""
        UserManagementScreen.setObjectName("UserManagementScreen")
        UserManagementScreen.resize(1200, 800)
        
        # Create central widget
        self.centralwidget = QWidget(UserManagementScreen)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create main layout
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)
        
        # Create header
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setMaximumHeight(100)
        self.header_layout = QVBoxLayout(self.header_widget)
        
        # Create title label
        self.title_label = QLabel("User Management")
        title_font = QFont()
        title_font.setFamily("Arial")
        title_font.setPointSize(24)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.header_layout.addWidget(self.title_label)
        
        # Add description label
        self.description_label = QLabel("Manage user accounts and permissions")
        desc_font = QFont()
        desc_font.setFamily("Arial")
        desc_font.setPointSize(12)
        self.description_label.setFont(desc_font)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.header_layout.addWidget(self.description_label)
        
        # Add header to main layout
        self.main_layout.addWidget(self.header_widget)
        
        # Create button layout
        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(10)
        
        # Create buttons
        self.back_button = QPushButton("Back")
        self.add_user_button = QPushButton("Add User")
        self.delete_button = QPushButton("Delete Selected")
        self.reset_flags_button = QPushButton("Reset Flags")
        self.view_reputation_button = QPushButton("View Reputation")
        
        # Style the buttons
        for button in [self.back_button, self.add_user_button, self.delete_button, 
                      self.reset_flags_button, self.view_reputation_button]:
            button.setMinimumHeight(40)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border-radius: 5px;
                    font-size: 14px;
                    padding: 5px 15px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
                QPushButton:pressed {
                    background-color: #1c6ea4;
                }
            """)
        
        # Add buttons to layout
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.add_user_button)
        self.button_layout.addWidget(self.delete_button)
        self.button_layout.addWidget(self.reset_flags_button)
        self.button_layout.addWidget(self.view_reputation_button)
        
        # Connect button signals to slots
        self.back_button.clicked.connect(self.back_clicked)
        self.add_user_button.clicked.connect(self.add_user_clicked)
        self.delete_button.clicked.connect(self.delete_user_clicked)
        self.reset_flags_button.clicked.connect(self.reset_flags_clicked)
        self.view_reputation_button.clicked.connect(self.view_reputation_clicked)
        
        # Add button layout to main layout
        self.main_layout.addLayout(self.button_layout)
        
        # Create table widget for users
        self.users_table = QTableWidget(self.centralwidget)
        self.users_table.setColumnCount(8)
        self.users_table.setHorizontalHeaderLabels([
            "Username", "First Name", "Last Name", "Email", "Admin", "Last Login", 
            "Flag Status", "Rep. Score"
        ])
        self.users_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.users_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.users_table.setSelectionMode(QTableWidget.SingleSelection)
        self.users_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.users_table.setAlternatingRowColors(True)
        self.users_table.verticalHeader().setVisible(False)
        
        # Add table to main layout
        self.main_layout.addWidget(self.users_table)
        
        # Set central widget
        UserManagementScreen.setCentralWidget(self.centralwidget)
        
        # Set text for UI elements
        self.set_text(UserManagementScreen)
        
        # Apply modern styling
        self.apply_styling()
    
    def set_text(self, UserManagementScreen):
        """Set the text for UI elements."""
        UserManagementScreen.setWindowTitle("Cypress - User Management")
        self.title_label.setText("User Management")
        self.description_label.setText("Manage user accounts and permissions")
        self.add_user_button.setText("Add User")
        self.delete_button.setText("Delete Selected")
        self.reset_flags_button.setText("Reset Flags")
        self.view_reputation_button.setText("View Reputation")
        self.back_button.setText("Back")
    
    def apply_styling(self):
        """Apply modern styling to UI elements."""
        # Set stylesheet for buttons
        button_style = """
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 5px;
                padding: 8px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c6ea4;
            }
        """
        
        self.add_user_button.setStyleSheet(button_style)
        self.back_button.setStyleSheet(button_style)
        
        # Set delete button to red
        delete_button_style = """
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 5px;
                padding: 8px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #a93226;
            }
        """
        self.delete_button.setStyleSheet(delete_button_style)
        
        # Set table style
        table_style = """
            QTableWidget {
                background-color: #ffffff;
                alternate-background-color: #f5f5f5;
                border: 1px solid #dcdcdc;
                border-radius: 5px;
                padding: 5px;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QHeaderView::section {
                background-color: #3498db;
                color: white;
                padding: 5px;
                border: none;
                font-weight: bold;
            }
        """
        self.users_table.setStyleSheet(table_style)


class UserManagementScreen(QMainWindow, Ui_UserManagementScreen):
    """
    Functional implementation of the User Management Screen.
    
    This class extends the UI definition with actual functionality, handling
    user interactions and connecting signals to slots.
    """
    
    def __init__(self):
        """Initialize the User Management Screen."""
        super(UserManagementScreen, self).__init__()
        self.setupUi(self)
        
        # Initialize reputation system
        self.reputation_system = get_reputation_system()
        
        # Apply modern styling
        self.apply_styling()
        
        # Set text and initial state
        self.set_text(self)
        
        # Load user data
        self.load_users()
        
        # Connect button signals to slots
        self.back_button.clicked.connect(self.back_clicked)
        self.add_user_button.clicked.connect(self.add_user_clicked)
        self.delete_button.clicked.connect(self.delete_user_clicked)
        self.reset_flags_button.clicked.connect(self.reset_flags_clicked)
        self.view_reputation_button.clicked.connect(self.view_reputation_clicked)
        
        # Initially disable edit, delete, and admin buttons until a user is selected
        self.delete_button.setEnabled(False)
        self.reset_flags_button.setEnabled(False)
        self.view_reputation_button.setEnabled(False)
        
        # Connect table selection to enable buttons
        self.users_table.itemSelectionChanged.connect(self.selection_changed)
    
    def load_users(self):
        """Load users from userData into the table."""
        global userData
        
        # Clear the table
        self.users_table.setRowCount(0)
        
        # Add each user to the table
        for i, user in enumerate(userData):
            if user:  # Skip empty entries
                self.users_table.insertRow(i)
                
                # Username
                username_item = QTableWidgetItem(user[5])
                self.users_table.setItem(i, 0, username_item)
                
                # First Name
                first_name_item = QTableWidgetItem(user[0])
                self.users_table.setItem(i, 1, first_name_item)
                
                # Last Name
                last_name_item = QTableWidgetItem(user[1])
                self.users_table.setItem(i, 2, last_name_item)
                
                # Email
                email_item = QTableWidgetItem(user[2])
                self.users_table.setItem(i, 3, email_item)
                
                # Admin Status - check index 8 for boolean value
                is_admin = "Yes" if user[8] is True else "No"
                admin_item = QTableWidgetItem(is_admin)
                if is_admin == "Yes":
                    admin_item.setForeground(QColor("#2ecc71"))  # Green for admins
                self.users_table.setItem(i, 4, admin_item)
                
                # Last Login (placeholder for now)
                last_login_item = QTableWidgetItem("N/A")
                self.users_table.setItem(i, 5, last_login_item)
                
                # Get reputation data for this user
                reputation = self.reputation_system.get_user_reputation(user[5])
                
                # Flag status
                flag_status = "Flagged" if reputation["flagged"] else "Good"
                flag_item = QTableWidgetItem(flag_status)
                flag_item.setTextAlignment(Qt.AlignCenter)
                
                # Color code the flag status
                if reputation["flagged"]:
                    flag_item.setBackground(QColor(255, 127, 127))  # Light red
                else:
                    flag_item.setBackground(QColor(187, 255, 187))  # Light green
                    
                self.users_table.setItem(i, 6, flag_item)
                
                # Reputation score
                score_item = QTableWidgetItem(str(reputation["score"]))
                score_item.setTextAlignment(Qt.AlignCenter)
                
                # Color code the score
                if reputation["score"] < 50:
                    score_item.setBackground(QColor(255, 127, 127))  # Light red
                elif reputation["score"] < 75:
                    score_item.setBackground(QColor(255, 255, 127))  # Light yellow
                else:
                    score_item.setBackground(QColor(187, 255, 187))  # Light green
                    
                self.users_table.setItem(i, 7, score_item)
    
    def selection_changed(self):
        """Handle when a user is selected in the table."""
        # Enable buttons if a row is selected
        selected_rows = self.users_table.selectedItems()
        if selected_rows:
            self.delete_button.setEnabled(True)
            self.reset_flags_button.setEnabled(True)
            self.view_reputation_button.setEnabled(True)
        else:
            self.delete_button.setEnabled(False)
            self.reset_flags_button.setEnabled(False)
            self.view_reputation_button.setEnabled(False)
    
    def get_selected_user_index(self):
        """Get the index of the selected user in userData."""
        global userData
        
        selected_items = self.users_table.selectedItems()
        if not selected_items:
            return -1
        
        row = selected_items[0].row()
        username = self.users_table.item(row, 0).text()
        
        # Find the user in userData
        for i, user in enumerate(userData):
            if user and user[5] == username:
                return i
        
        return -1
    
    def add_user_clicked(self):
        """Handle when the Add User button is clicked."""
        global userData
        
        dialog = UserDialog(self, "Add User")
        if dialog.exec_() == QDialog.Accepted:
            # Get user data from dialog
            first_name = dialog.first_name_input.text()
            last_name = dialog.last_name_input.text()
            email = dialog.email_input.text()
            username = dialog.username_input.text()
            password = dialog.password_input.text()
            is_admin = dialog.admin_checkbox.isChecked()
            
            # Check if username already exists
            for user in userData:
                if user and user[5] == username:
                    QMessageBox.warning(
                        self,
                        "Username Exists",
                        f"The username '{username}' already exists. Please choose a different username."
                    )
                    return
            
            # Add user to userData - format: [FirstName, LastName, Address, Phone, Email, Username, Password, Reports Count, isAdmin]
            userData.append([first_name, last_name, "", "", email, username, password, 0, is_admin])
            
            # Save userData to file
            self.save_user_data()
            
            # Reload users table
            self.load_users()
            
            # Show success message
            QMessageBox.information(
                self,
                "User Added",
                f"User '{username}' has been added successfully."
            )
    
    def delete_user_clicked(self):
        """Handle when the Delete User button is clicked."""
        global userData
        
        user_index = self.get_selected_user_index()
        if user_index < 0:
            return
        
        # Get username
        username = userData[user_index][5]
        
        # Confirm deletion
        reply = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete user '{username}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Delete user from userData
            userData[user_index] = None
            
            # Save userData to file
            self.save_user_data()
            
            # Reload users table
            self.load_users()
            
            # Show success message
            QMessageBox.information(
                self,
                "User Deleted",
                f"User '{username}' has been deleted successfully."
            )
    
    def reset_flags_clicked(self):
        """Handle when the Reset Flags button is clicked."""
        selected_index = self.get_selected_user_index()
        if selected_index >= 0:
            username = userData[selected_index][5]
            
            # Confirm reset
            reply = QMessageBox.question(
                self,
                "Reset User Flags",
                f"Are you sure you want to reset flags for user '{username}'?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                # Reset the user's flags
                self.reputation_system.reset_user_flags(username)
                
                # Show confirmation
                QMessageBox.information(
                    self,
                    "Flags Reset",
                    f"Flags for user '{username}' have been reset successfully."
                )
                
                # Refresh the table
                self.load_users()
                
        else:
            QMessageBox.warning(
                self,
                "No Selection",
                "Please select a user to reset flags for."
            )
    
    def view_reputation_clicked(self):
        """Handle when the View Reputation button is clicked."""
        selected_index = self.get_selected_user_index()
        if selected_index >= 0:
            username = userData[selected_index][5]
            
            # Get reputation data
            reputation = self.reputation_system.get_user_reputation(username)
            
            # Show reputation data
            QMessageBox.information(
                self,
                "User Reputation",
                f"Username: {username}\n"
                f"Flagged: {reputation['flagged']}\n"
                f"Score: {reputation['score']}"
            )
        else:
            QMessageBox.warning(
                self,
                "No Selection",
                "Please select a user to view their reputation."
            )
    
    def save_user_data(self):
        """Save userData to file."""
        global userData
        
        # Filter out None values
        filtered_data = [user for user in userData if user]
        
        # Save to file
        with open("users.txt", "w") as f:
            for user in filtered_data:
                f.write(",".join(map(str, user)) + "\n")
    
    def back_clicked(self):
        """Handle when the Back button is clicked."""
        global isAdminUser  # Declare isAdminUser as global in this method
        
        self.hide()
        from main_ui import MyMainScreen
        
        # Ensure we're importing the global variable
        import main_ui
        
        # Make sure isAdminUser is True before creating the main screen
        main_ui.isAdminUser = True
        
        self.next = MyMainScreen()
        self.next.showFullScreen()


class UserDialog(QDialog):
    """Dialog for adding or editing users."""
    
    def __init__(self, parent=None, title="User"):
        """Initialize the dialog."""
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(400)
        
        # Create layout
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        
        # Create form layout
        form_layout = QFormLayout()
        form_layout.setSpacing(10)
        
        # Create input fields
        self.first_name_input = QLineEdit()
        self.last_name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.admin_checkbox = QCheckBox("Administrator")
        
        # Add fields to form layout
        form_layout.addRow("First Name:", self.first_name_input)
        form_layout.addRow("Last Name:", self.last_name_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Username:", self.username_input)
        form_layout.addRow("Password:", self.password_input)
        form_layout.addRow("", self.admin_checkbox)
        
        # Add form layout to main layout
        layout.addLayout(form_layout)
        
        # Create button box
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.validate_and_accept)
        button_box.rejected.connect(self.reject)
        
        # Add button box to main layout
        layout.addWidget(button_box)
        
        # Apply styling
        self.apply_styling()
    
    def apply_styling(self):
        """Apply modern styling to the dialog."""
        self.setStyleSheet("""
            QDialog {
                background-color: #f5f5f5;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #dcdcdc;
                border-radius: 4px;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
            QLabel {
                font-weight: bold;
            }
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
        """)
    
    def validate_and_accept(self):
        """Validate inputs before accepting."""
        # Check if required fields are filled
        if not self.first_name_input.text():
            QMessageBox.warning(self, "Missing Information", "Please enter a first name.")
            return
        
        if not self.last_name_input.text():
            QMessageBox.warning(self, "Missing Information", "Please enter a last name.")
            return
        
        if not self.email_input.text():
            QMessageBox.warning(self, "Missing Information", "Please enter an email address.")
            return
        
        if not self.username_input.text():
            QMessageBox.warning(self, "Missing Information", "Please enter a username.")
            return
        
        # Only require password for new users (username field is editable)
        if not self.username_input.isReadOnly() and not self.password_input.text():
            QMessageBox.warning(self, "Missing Information", "Please enter a password.")
            return
        
        # Accept the dialog
        self.accept()
