import sys
import ctypes
import json
import os
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import FrontScreen
import RegisterScreen
import LoginScreen
import ReportScreen
import SuggestScreen
import MainScreen
import MapDialog  # Import the MapDialog module
import MyReports
import ui_utils
from PyQt5 import QtWidgets
import datetime
import re

# This is the array of user information, this array does not include user security questions and answers
global userData
userData = []
# Format: [FirstName, LastName, Address, Phone, Email, Username, Password, Reports Count, isAdmin]
userData.append(
    [
        "User",
        "Name",
        "Test Address Street",
        "4161234567",
        "user@toronto.ca",
        "user",
        "user123",
        0,
        False,
    ]
)  # Regular user

userData.append(
    [
        "Admin",
        "Name",
        "City Hall",
        "4162223333",
        "admin@toronto.ca",
        "admin",
        "admin123",
        0,
        True,
    ]
)  # Admin user
# userData.append(['Briana', 'Alice', '123 Chip', '123456789',briannaMail56@gmail.com,'briChip'\
# , 'pass123WORD',0]) #For testing

# This array stores security question and answer info about each user (Only needed for register/login purposes)
global userQData
userQData = []

# This is the variable that holds the user name of the user currently logged in
# It will be None if no one is logged in
global userAccount
userAccount = None

# This variable indicates if the current user is an admin
global isAdminUser
isAdminUser = False

# Track the active user index
global active_user
active_user = 0  # Set to first user by default for testing

# Initialize empty reports list for storing submitted reports
global reports
reports = []

# Array of problem types for the report screen
global allProblems
allProblems = [
    "Water/Electricity Outage",
    "Road Damage (Potholes)",
    "Graffiti and Vandalism",
    "Street Erosion",
    "Fallen Trees/Branches",
    "Street Flooding",
    "Public Health Hazard",
    "Roadway Obstruction",
]

global userReports
userReports = {}  # Initialize userReports dictionary to store user reports

global suggestions
suggestions = {}  # Initialize suggestions dictionary to store report suggestions

class MyFrontScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = FrontScreen.Ui_FrontScreen()
        self.ui.setupUi(self)
        ui_utils.setup_modern_buttons(self)

        # Hide the French button
        if hasattr(self.ui, "french_button"):
            self.ui.french_button.setVisible(False)

        # Improve button size to prevent text cutoff
        self.ui.english_button.setMinimumSize(250, 60)

        # Set button styling
        button_style = """
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """
        self.ui.english_button.setStyleSheet(button_style)

        # Rename button to just "Start"
        self.ui.english_button.setText("Start")

        # Connect buttons to their respective functions
        self.ui.english_button.clicked.connect(self.eng_clicked)
        
        # Connect the exit button if it exists
        if hasattr(self.ui, "exit_button"):
            self.ui.exit_button.clicked.connect(self.exit_application)
        
        # Remove French button connection
        # self.ui.french_button.clicked.connect(self.fre_clicked)

        # Show in full screen mode
        self.showFullScreen()

    def eng_clicked(self):
        self.hide()
        self.next = MyLoginScreen()
        self.next.show()

    # Keep this function for backward compatibility, but it won't be used
    def fre_clicked(self):
        self.eng_clicked()
        
    def exit_application(self):
        """Exit the application when the exit button is clicked."""
        # Show a confirmation dialog
        reply = QtWidgets.QMessageBox.question(
            self, 
            'Exit Confirmation',
            'Are you sure you want to exit the application?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        
        if reply == QtWidgets.QMessageBox.Yes:
            QtWidgets.QApplication.quit()


class MyMainScreen(QMainWindow):
    """
    Main screen implementation with functionality.
    
    This class extends the UI definition with actual functionality,
    handling user interactions and navigation between different screens.
    """
    
    def __init__(self):
        """Initialize the main screen with functionality."""
        super().__init__()
        self.ui = MainScreen.Ui_MainScreen()
        self.ui.setupUi(self)
        
        # Apply modern styling to buttons
        if hasattr(ui_utils, "setup_modern_buttons"):
            ui_utils.setup_modern_buttons(self)
        
        # Apply shadow effect to frame if it exists
        if hasattr(self.ui, "frame"):
            ui_utils.create_shadow_effect(self.ui.frame)

        # Set window to full screen
        self.showMaximized()

        # Connect button signals to slots
        self.ui.go_button.clicked.connect(self.go_clicked)
        self.ui.exit_button.clicked.connect(self.exit_clicked)

        # Handle admin mode
        if not isAdminUser:
            # Hide admin-specific UI elements for regular users
            if hasattr(self.ui, "admin_label"):
                self.ui.admin_label.hide()
            
            # Hide admin-specific buttons
            if hasattr(self.ui, "admin_reports_button"):
                self.ui.admin_reports_button.hide()
            if hasattr(self.ui, "user_management_button"):
                self.ui.user_management_button.hide()
            if hasattr(self.ui, "system_settings_button"):
                self.ui.system_settings_button.hide()
        else:
            # In admin mode, show admin label and hide regular user options
            if hasattr(self.ui, "admin_label"):
                self.ui.admin_label.show()
            
            # Hide regular user options in admin mode
            self.ui.report_button.hide()
            self.ui.suggest_button.hide()
            self.ui.myReports_button.hide()
            
            # Keep logout button visible for admins
            self.ui.logout_button.show()

    def go_clicked(self):
        """Handle navigation when the Go button is clicked."""
        # Navigate to the selected screen based on which radio button is checked
        if self.ui.report_button.isChecked():
            self.hide()
            self.next = MyReportScreen()
            self.next.showFullScreen()
        elif self.ui.suggest_button.isChecked():
            self.hide()
            self.next = MySuggestScreen()
            self.next.showFullScreen()
        elif self.ui.myReports_button.isChecked():
            self.hide()
            self.next = MyUserReports()
            self.next.showFullScreen()
        elif hasattr(self.ui, "admin_reports_button") and self.ui.admin_reports_button.isChecked():
            self.hide()
            self.next = AdminReportViewer()
            self.next.showFullScreen()
        elif hasattr(self.ui, "user_management_button") and self.ui.user_management_button.isChecked():
            self.hide()
            from UserManagementScreen import UserManagementScreen
            self.next = UserManagementScreen()
            self.next.showFullScreen()
        elif hasattr(self.ui, "system_settings_button") and self.ui.system_settings_button.isChecked():
            self.hide()
            from SystemSettingsScreen import SystemSettingsScreen
            self.next = SystemSettingsScreen()
            self.next.showFullScreen()
        elif self.ui.logout_button.isChecked():
            self.logout_clicked()

    def logout_clicked(self):
        global userAccount
        global isAdminUser
        userAccount = None
        isAdminUser = False
        self.hide()
        self.next = MyLoginScreen()
        self.next.showFullScreen()
        
    def exit_clicked(self):
        """Exit the application after confirmation."""
        reply = QtWidgets.QMessageBox.question(
            self, 
            'Exit Confirmation',
            'Are you sure you want to exit the application?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        
        if reply == QtWidgets.QMessageBox.Yes:
            QtWidgets.QApplication.quit()


class MyLoginScreen(QMainWindow):
    """
    Login screen implementation with functionality.
    
    This class extends the UI definition with actual functionality,
    handling user authentication and navigation.
    """
    
    def __init__(self):
        """Initialize the login screen with functionality."""
        super().__init__()
        self.ui = LoginScreen.Ui_LoginScreen()
        self.ui.setupUi(self)
        
        # Apply modern styling to buttons
        if hasattr(ui_utils, "setup_modern_buttons"):
            ui_utils.setup_modern_buttons(self)
        
        # Apply shadow effect to frame if it exists
        if hasattr(self.ui, "form_container"):
            ui_utils.create_shadow_effect(self.ui.form_container)
        
        # Connect button signals to slots
        self.ui.login_button.clicked.connect(self.login_clicked)
        self.ui.cancel_button.clicked.connect(self.back_clicked)
        self.ui.register_button.clicked.connect(self.register_clicked)
        self.ui.forgot_button.clicked.connect(self.forgot_clicked)
        self.ui.exit_button.clicked.connect(self.exit_clicked)
        
        # Change cancel button text to back
        self.ui.cancel_button.setText("Back")
        
        # Show in full screen mode
        self.showFullScreen()

    def back_clicked(self):
        self.hide()
        self.next = MyFrontScreen()
        self.next.showFullScreen()

    def login_clicked(self):
        global userAccount
        global active_user
        global isAdminUser

        userNm = self.ui.username_input.text()
        passWd = self.ui.password_input.text()

        result = self.isValidLogin([userNm, passWd])
        if result == "granted":
            # Set userAccount to the username of the logged-in user
            userAccount = userNm
            
            # Log successful login
            print(f"Login successful for user: {userAccount}, Admin: {isAdminUser}")
            
            self.hide()
            self.next = MyMainScreen()
            self.next.showFullScreen()
        else:
            # Create a more user-friendly error message
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Login Failed")
            
            if result == "denied":
                error_dialog.setText("Invalid username or password.")
                error_dialog.setInformativeText("Please check your credentials and try again.")
            else:  # This would be for any other error states
                error_dialog.setText("Login Error")
                error_dialog.setInformativeText(result)
                
            error_dialog.setStandardButtons(QMessageBox.Ok)
            error_dialog.exec_()

    def register_clicked(self):
        self.hide()
        self.next = MyRegisterScreen()
        self.next.showFullScreen()

    def isValidLogin(self, listInfo):
        global userAccount
        global isAdminUser
        userAccount = None
        isAdminUser = False
        if listInfo[0] == "" or listInfo[1] == "":
            return "blank"
        for i in range(len(userData)):
            if userData[i][5] == listInfo[0]:
                if userData[i][6] == listInfo[1]:
                    userAccount = listInfo[0]
                    # Set admin status based on user data
                    if len(userData[i]) > 8:
                        isAdminUser = userData[i][8]
                        print(
                            f"User logged in as: {userAccount}, Admin flag in userData: {userData[i][8]}"
                        )
                    else:
                        isAdminUser = False
                        print(
                            f"User logged in as: {userAccount}, No admin flag in userData"
                        )

                    print(
                        f"Login successful! User: {userAccount}, Admin status: {isAdminUser}"
                    )
                    return "granted"
                else:
                    return "denied"
        return "denied"

    def forgot_clicked(self):
        """Handle forgotten password."""
        # Display a message box informing the user that this feature is not yet implemented
        QtWidgets.QMessageBox.information(
            self,
            "Forgot Password",
            "The forgot password feature is not yet implemented."
        )
        
    def exit_clicked(self):
        """Exit the application after confirmation."""
        reply = QtWidgets.QMessageBox.question(
            self, 
            'Exit Confirmation',
            'Are you sure you want to exit the application?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        
        if reply == QtWidgets.QMessageBox.Yes:
            QtWidgets.QApplication.quit()


class MyRegisterScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        userAccount = None
        self.ui = RegisterScreen.Ui_RegisterScreen()
        self.ui.setupUi(self)
        ui_utils.setup_modern_buttons(self)
        self.ui.register_button.clicked.connect(self.register_clicked)
        self.ui.cancel_button.clicked.connect(self.back_clicked)
        self.ui.exit_button.clicked.connect(self.exit_clicked)

        # Set up input validation
        self.setup_validation()
        
        # Change cancel button text to back
        self.ui.cancel_button.setText("Back")
        
        # Show in full screen mode
        self.showFullScreen()
    
    def setup_validation(self):
        """Set up input field validation and constraints"""
        # Phone number validation - only allow digits
        self.ui.phone_1.setMaxLength(3)  # Area code (3 digits)
        self.ui.phone_2.setMaxLength(3)  # First 3 digits
        self.ui.phone_3.setMaxLength(4)  # Last 4 digits
        
        # Set up validators for phone fields (digits only)
        digit_validator = QRegExpValidator(QRegExp("[0-9]+"))
        self.ui.phone_1.setValidator(digit_validator)
        self.ui.phone_2.setValidator(digit_validator)
        self.ui.phone_3.setValidator(digit_validator)
        
        # Add placeholder text to fields
        self.ui.first_name.setPlaceholderText("Enter your first name")
        self.ui.last_name.setPlaceholderText("Enter your last name")
        self.ui.address.setPlaceholderText("Enter your full address")
        self.ui.phone_1.setPlaceholderText("123")
        self.ui.phone_2.setPlaceholderText("456")
        self.ui.phone_3.setPlaceholderText("7890")
        self.ui.email_address.setPlaceholderText("your.email")
        self.ui.username.setPlaceholderText("Choose a username")
        self.ui.password.setPlaceholderText("Choose a secure password")

    def back_clicked(self):
        if userAccount is not None:
            self.hide()
            self.next = MyMainScreen()
            self.next.showFullScreen()
        else:
            self.hide()
            self.next = MyLoginScreen()
            self.next.showFullScreen()

    def register_clicked(self):
        # Get user input from form fields
        firstName = self.ui.first_name.text().strip()
        lastName = self.ui.last_name.text().strip()
        address = self.ui.address.text().strip()
        phone = self.ui.phone_1.text() + "-" + self.ui.phone_2.text() + "-" + self.ui.phone_3.text()
        email = self.ui.email_address.text().strip() + "@cypress.on.ca"
        userName = self.ui.username.text().strip()
        password = self.ui.password.text()

        # Add the elements to a list that will be added to userData if it is correct
        listInfo = [
            firstName,
            lastName,
            address,
            phone,
            email,
            userName,
            password,
            0,
            False,
        ]

        # Validate form before proceeding
        validation_result = self.isValidRegister(listInfo)
        if validation_result != True:
            # Show error message with detailed feedback
            msg = QMessageBox()
            msg.setWindowTitle("Registration Error")
            msg.setIcon(QMessageBox.Warning)
            msg.setText(validation_result)
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: #f8f9fa;
                }
                QMessageBox QLabel {
                    color: #2c3e50;
                }
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border-radius: 5px;
                    padding: 5px 15px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)
            msg.exec_()
            
            # Reset the password field for security
            if "Password" in validation_result:
                self.ui.password.clear()
        else:
            # Show security question dialog
            self.SQ = RegisterScreen.MyDialog()
            self.hide()
            self.SQ.exec_()
            
            # Get security question and answer
            sq_lis = [
                self.SQ.ui.security_question.text().strip(),
                self.SQ.ui.security_answer.text().strip(),
            ]
            
            # Validate security question and answer
            if len(sq_lis[0]) > 0 and len(sq_lis[1]) > 0:
                # Add security question to user data
                userQData.append(sq_lis)
                
                # Set global user account
                global userAccount
                userAccount = userName
                
                # Show success message
                msg = QMessageBox()
                msg.setWindowTitle("Registration Successful")
                msg.setIcon(QMessageBox.Information)
                msg.setText(f"Welcome, {firstName}! Your account has been created successfully.")
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: #f8f9fa;
                    }
                    QMessageBox QLabel {
                        color: #2c3e50;
                    }
                    QPushButton {
                        background-color: #27ae60;
                        color: white;
                        border-radius: 5px;
                        padding: 5px 15px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #2ecc71;
                    }
                """)
                msg.exec_()
                
                # Navigate to main screen
                self.back_clicked()
            else:
                # Remove the user if security question/answer is invalid
                userData.pop()
                self.show()
                
                # Show error message
                msg = QMessageBox()
                msg.setWindowTitle("Registration Error")
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Please provide both a security question and answer.")
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: #f8f9fa;
                    }
                    QMessageBox QLabel {
                        color: #2c3e50;
                    }
                    QPushButton {
                        background-color: #e74c3c;
                        color: white;
                        border-radius: 5px;
                        padding: 5px 15px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #c0392b;
                    }
                """)
                msg.exec_()

    def exit_clicked(self):
        """Exit the application after confirmation."""
        reply = QtWidgets.QMessageBox.question(
            self, 
            'Exit Confirmation',
            'Are you sure you want to exit the application?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        
        if reply == QtWidgets.QMessageBox.Yes:
            QtWidgets.QApplication.quit()

    def isValidRegister(self, listInfo):
        """
        Validate registration information
        
        Args:
            listInfo: List of user information to validate
            
        Returns:
            True if valid, error message string if invalid
        """
        # Check for empty fields
        field_names = ["First Name", "Last Name", "Address", "Phone Number", "Email", "Username", "Password"]
        for i in range(0, len(field_names)):
            element = listInfo[i]
            if len(element) == 0 or element.isspace():
                return f"{field_names[i]} cannot be empty"

        # Validate phone number format (###-###-####)
        phone = listInfo[3]
        if not (len(phone) == 12 and phone[3] == '-' and phone[7] == '-' and 
                phone.replace('-', '').isdigit() and len(phone.replace('-', '')) == 10):
            return "Phone number must be in format: ###-###-####"
            
        # Validate email format
        email = listInfo[4]
        if not email.endswith("@cypress.on.ca") or '@' not in email:
            return "Invalid email format"
            
        # Validate username (alphanumeric, no spaces)
        username = listInfo[5]
        if not username.isalnum():
            return "Username must contain only letters and numbers (no spaces or special characters)"
            
        # Password validation
        password = listInfo[6]
        
        # Check password length
        if len(password) < 8:
            return "Password must be at least 8 characters long"
            
        # Check password complexity
        has_digit = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        
        if not (has_digit and has_upper and has_lower):
            missing = []
            if not has_digit:
                missing.append("at least one number")
            if not has_upper:
                missing.append("at least one uppercase letter")
            if not has_lower:
                missing.append("at least one lowercase letter")
                
            return f"Password must contain {', '.join(missing)}"
            
        # Check if username is already taken
        for user in userData:
            if user[5].lower() == username.lower():
                return "Username is already taken. Please choose a different username."
                
        # All validation passed, add user to userData
        userData.append(listInfo)
        return True


class MyReportScreen(QMainWindow):
    def __init__(self):
        global selectedAddress, allProblems, active_user, reports, Ui_ReportScreen
        super().__init__()
        self.ui = ReportScreen.Ui_ReportScreen()
        self.ui.setupUi(self)
        ui_utils.setup_modern_buttons(self)

        # Set up file dialog connection for image attachment
        self.ui.browse_button.clicked.connect(self.browse_image)
        self.ui.drop_area.mousePressEvent = self.drop_area_clicked

        # Set up map button functionality
        self.ui.map_button.clicked.connect(self.open_map)

        # Set up drag and drop support for the image area
        self.ui.drop_area.setAcceptDrops(True)
        self.ui.drop_area.dragEnterEvent = self.dragEnterEvent
        self.ui.drop_area.dropEvent = self.dropEvent

        # Initialize image path
        self.image_path = None

        prblm_btn = [
            self.ui.utility_failures_button,
            self.ui.potholes_button,
            self.ui.vandalism_button,
            self.ui.erroded_streets_button,
            self.ui.tree_collapse_button,
            self.ui.flooded_streets_button,
            self.ui.mould_button,
            self.ui.garbage_button,
        ]

        # Connect the report and cancel buttons
        self.ui.report_button.clicked.connect(self.send_clicked)
        self.ui.cancel_button.clicked.connect(self.back_clicked)

        # Change cancel button text to back
        self.ui.cancel_button.setText("Back")

        self.selectedProblems = None

        for index, btn in enumerate(prblm_btn):
            btn.setChecked(False)
            btn.clicked.connect(
                lambda state, i=index: self.selectedProblemBtn(state, i)
            )

    def browse_image(self):
        """Open file dialog to select an image"""
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")
        file_dialog.setViewMode(QFileDialog.Detail)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.image_path = selected_files[0]
                self.display_selected_image()

    def drop_area_clicked(self, event):
        """Handle click on the drop area"""
        self.browse_image()

    def dragEnterEvent(self, event):
        """Handle drag enter events for image drops"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        """Handle drop events for images"""
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            self.image_path = url.toLocalFile()
            self.display_selected_image()
            event.acceptProposedAction()

    def display_selected_image(self):
        """Display the selected image in the drop area"""
        if self.image_path:
            pixmap = QPixmap(self.image_path)
            if not pixmap.isNull():
                # Resize pixmap to fit drop area while maintaining aspect ratio
                pixmap = pixmap.scaled(
                    200, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                self.ui.drop_area.setPixmap(pixmap)
                self.ui.drop_area.setAlignment(Qt.AlignCenter)
            else:
                # If loading fails, show error message
                self.ui.drop_area.setText("Failed to load image")

    def selectedProblemBtn(self, state, index):
        if state:
            self.selectedProblems = allProblems[index]

    def send_clicked(self):
        # Save report information along with the image
        if self.selectedProblems and self.ui.address_input.text():
            address = self.ui.address_input.text()
            problem_type = self.selectedProblems
            
            # Check for duplicate reports
            if is_duplicate_report(address, problem_type):
                # Show duplicate warning message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"A report for '{problem_type}' at '{address}' already exists.\n\nDuplicate reports are not allowed.")
                msg.setWindowTitle("Duplicate Report")
                msg.exec_()
                return
            
            report_entry = {
                "address": address,
                "problem": problem_type,
                "description": self.ui.description_input.toPlainText(),
                "image_path": self.image_path,
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "username": userData[active_user][5],
                "status": "Pending",  # Add default status
            }

            # Add to reports
            try:
                reports.append(report_entry)
                # Save reports to file
                save_reports_to_file()
                
                # Add to userReports dictionary for the current user
                global userReports, userAccount
                if userAccount not in userReports:
                    userReports[userAccount] = []
                
                # Create the report entry in the format expected by MyUserReports
                user_report_entry = [report_entry["address"], report_entry["problem"], report_entry["status"]]
                
                # Only add the report if it's not already in the user's list
                if user_report_entry not in userReports[userAccount]:
                    userReports[userAccount].append(user_report_entry)
                
                # Show success message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Report submitted successfully!")
                msg.setWindowTitle("Success")
                msg.exec_()
                # Go back to main screen instead of closing
                self.hide()
                self.next = MyMainScreen()
                self.next.showFullScreen()
            except Exception as e:
                # Show error message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(f"Error submitting report: {str(e)}")
                msg.setWindowTitle("Error")
                msg.exec_()
        else:
            # Show validation error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please enter an address and select a problem type.")
            msg.setWindowTitle("Validation Error")
            msg.exec_()

    def back_clicked(self):
        self.hide()
        self.next = MyMainScreen()
        self.next.showFullScreen()

    def open_map(self):
        """Open the map dialog to select a location"""
        map_dialog = MapDialog.MapDialog(self)
        map_dialog.addressSelected.connect(self.set_address)
        map_dialog.exec_()

    def set_address(self, address):
        """Set the address field with the selected location"""
        self.ui.address_input.setText(address)


class MyProfileScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global userData
        global userAccount
        self.userInfo = []
        for i in range(len(userData)):
            if userData[i][5] == userAccount:
                self.userInfo = userData[i] + userQData[i]
                break
        self.ui = ProfileScreen.Ui_ProfileScreen()
        self.ui.setupUi(self)
        ui_utils.setup_modern_buttons(self)
        self.ui.edit_button.clicked.connect(self.resetUpUi_clicked)
        self.ui.delete_button.clicked.connect(self.delete_clicked)
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)

    def cancel_clicked(self):
        self.hide()
        self.next = MyMainScreen()
        self.next.showFullScreen()

    def delete_clicked(self):
        # Make user answer security question from logout page
        # Get the userNum from userData
        userNum = -1
        for user in userData:
            userNum += 1
            if user[5] == userAccount:
                break
        # Get the user question
        question = userQData[userNum][0]
        # Display the user question
        self.SQ = LoginScreen.MyDialog(question)
        self.SQ.exec_()
        answer = self.SQ.ui.security_answer.text()
        # get info with : self.SQ.ui.security_answer.text() and self.SQ.ui.security_question.text()
        # Check to see if answer is correct
        if userQData[userNum][1] == answer:
            # Then you can ask the user if they want to delete the report
            warn = QMessageBox()
            warn.setIcon(QMessageBox.Warning)
            warn.setText("Are you sure you want to delete your profile?")
            warn.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            warn.buttonClicked.connect(self.popup_button)
            warn.exec_()
            # userAccount=None
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Incorrect Security Response")
            msg.setText(
                "Security answer is incorrect. You may not delete your account at this time."
            )
            msg.exec_()

    def popup_button(self, btn):
        # Delete profile here if the user clicks yes
        if btn.text() == "&Yes":
            # Get the userNum from userData
            userNum = -1
            for user in userData:
                userNum += 1
                if user[5] == userAccount:
                    break
            # Delete userData with userNum
            del userData[userNum]
            # Delete userQData with userNum
            del userQData[userNum]
            # Return to the main page where userAccount will be equal to 0
            self.hide()
            self.next = MyFrontScreen()
            self.next.showFullScreen()

    def resetUpUi_clicked(self):
        # print(self.ui.edit_button.text())
        if self.ui.state == "edit":
            self.ui.state = "save"
            # self.ui.edit_button.setText("SAVE PROFILE")
            # Prompt the user
            msg = QMessageBox()
            msg.setText(
                "All information may be changed except for the following:\n - Username \
                        \n - Security question \n - Security answer"
            )
            msg.exec_()
            self.ui.first_name.setReadOnly(False)
            self.ui.last_name.setReadOnly(False)
            self.ui.address.setReadOnly(False)
            self.ui.phone.setReadOnly(False)
            self.ui.email_address.setReadOnly(False)
            self.ui.username.setReadOnly(True)
            self.ui.password.setReadOnly(False)
            self.ui.security_question.setReadOnly(True)
            self.ui.security_answer.setReadOnly(True)
            # Disable the delete button
            self.ui.delete_button.setDisabled(True)

        else:
            # Save by updating user information
            firstName = self.ui.first_name.text()
            lastName = self.ui.last_name.text()
            address = self.ui.address.text()
            phone = self.ui.phone.text()
            email = self.ui.email_address.text()
            userName = self.ui.username.text()
            password = self.ui.password.text()
            # securQuestion=self.ui.security_question.toPlainText()
            # securAnswer=self.ui.security_answer.toPlainText()

            listInfo = [
                firstName,
                lastName,
                address,
                phone,
                email,
                userName,
                password,
                0,
            ]

            check = self.checkReset(listInfo)
            if isinstance(check, str) == True:
                msg = QMessageBox()
                msg.setText(self.checkReset(listInfo))
                msg.exec_()
            else:
                self.ui.state = "edit"
                # Tell user changes have been made
                msg = QMessageBox()
                msg.setWindowTitle(" ")
                msg.setText("Information changed successfully.")
                msg.exec_()
                # Go back to the main page
                self.cancel_clicked()

    def checkReset(self, listInfo):
        foundNum = False  # If a number has been found in the password
        foundUpper = False  # If an uppercase letter has been found in password
        foundLower = False  # If a lowercase letter has been found in password

        # Make sure no fields are empty, if any are empty return false
        for i in range(0, len(listInfo) - 1):
            element = listInfo[i]
            if len(element) == 0:
                return "Not all fields are filled out correctly"

        # If the length of password is less than 8 chars return false
        if len(listInfo[6]) < 8:
            return "Length of password is too short"

        # Go through each character in password to check requirements
        for letter in listInfo[6]:
            # Check for a number
            if letter.isnumeric():
                foundNum = True
            # Check for an uppercase letter
            if letter.isupper():
                foundUpper = True
            # Check for an lowercase letter
            if letter.islower():
                foundLower = True

        # Check if the password is valid (field 6)
        if foundNum == False or foundUpper == False or foundLower == False:
            return "Password is missing at least one of the following:\n - 1 number \n - 1 uppercase letter\
                    \n - 1 lowercase letter"

        # If userData is empty add this as the first element
        if len(userData) == 0:
            userData.append(listInfo)
            return True

        # If it is not the first element in userData check if the username is free (field 5)
        for user in userData:
            if user[5] == listInfo[5] and listInfo[5] != userAccount:
                return "Username is already taken"

        # Get the userNum from userData
        userNum = -1
        for user in userData:
            userNum += 1
            if user[5] == userAccount:
                break

        # Since the username is free and the password is valid modify the current userData profile
        for i in range(len(userData)):
            if i == userNum:
                for j in range(7):
                    userData[i][j] = listInfo[j]

        return userNum


class MyUserReports(QMainWindow):
    """
    User Reports screen implementation with functionality.
    
    This class provides the functionality for users to view, edit, and delete
    their submitted reports. It displays reports in a scrollable area and
    handles user interactions with the reports.
    """
    
    def __init__(self):
        """Initialize the user reports screen with functionality."""
        super().__init__()
        
        # Initialize UI from the MyReports module
        self.ui = MyReports.Ui_MyReports()
        self.ui.setupUi(self)
        
        # Load the latest reports from file to ensure we have the most up-to-date data
        load_reports_from_file()
        
        # Check if user exists in userReports dictionary
        if userAccount not in userReports:
            userReports[userAccount] = []
        
        # Store the user's reports
        self.prblm_lis = userReports[userAccount]
        
        # Connect button signals to slots
        self.ui.back_button.clicked.connect(self.back_clicked)
        self.ui.delete_button.clicked.connect(self.delete_clicked)
        
        # Don't try to hide a non-existent status button
        # self.ui.status_button.hide()
        
        # Initially disable delete button until a report is selected
        self.ui.delete_button.setEnabled(False)
        
        # Display the user's reports
        self.display_reports()
    
    def display_reports(self):
        """Display the user's reports in the scrollable area."""
        # Clear any existing widgets in the scroll area
        for i in reversed(range(self.ui.reports_layout.count())):
            widget = self.ui.reports_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        
        # If user has no reports, display a message
        if not self.prblm_lis:
            no_reports_label = QtWidgets.QLabel("You have no reports to display.")
            no_reports_label.setStyleSheet("font-size: 14pt; padding: 20px;")
            no_reports_label.setAlignment(Qt.AlignCenter)
            self.ui.reports_layout.addWidget(no_reports_label)
            return
        
        # Create a widget for each report
        for i, report in enumerate(self.prblm_lis):
            # Create a frame for the report
            report_frame = QtWidgets.QFrame()
            report_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            report_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            
            # Apply alternating row colors for better readability
            if i % 2 == 0:
                report_frame.setStyleSheet("background-color: #f0f0f0; padding: 10px; margin: 5px;")
            else:
                report_frame.setStyleSheet("background-color: #e0e0e0; padding: 10px; margin: 5px;")
            
            # Create horizontal layout for the report
            report_layout = QtWidgets.QHBoxLayout(report_frame)
            
            # Add radio button for selection
            radio_button = QtWidgets.QRadioButton()
            radio_button.setObjectName(f"report_{i}")
            radio_button.toggled.connect(self.prblm_clicked)
            report_layout.addWidget(radio_button)
            
            # Add problem type label
            problem_label = QtWidgets.QLabel(report[1])
            problem_label.setStyleSheet("font-weight: bold; font-size: 12pt;")
            problem_label.setMinimumWidth(200)
            report_layout.addWidget(problem_label)
            
            # Add address label
            address_label = QtWidgets.QLabel(report[0])
            address_label.setStyleSheet("font-size: 12pt;")
            address_label.setWordWrap(True)
            report_layout.addWidget(address_label)
            
            # Add status label with appropriate color based on status
            status = report[2] if len(report) > 2 else "Pending"
            status_label = QtWidgets.QLabel(status)
            
            # Set color based on status
            if status == "Pending":
                status_label.setStyleSheet("font-size: 12pt; color: #f39c12; font-weight: bold;") # Orange
            elif status == "In Progress":
                status_label.setStyleSheet("font-size: 12pt; color: #3498db; font-weight: bold;") # Blue
            elif status == "Resolved":
                status_label.setStyleSheet("font-size: 12pt; color: #27ae60; font-weight: bold;") # Green
            elif status == "Closed":
                status_label.setStyleSheet("font-size: 12pt; color: #7f8c8d; font-weight: bold;") # Gray
            else:
                status_label.setStyleSheet("font-size: 12pt; color: #3498db; font-weight: bold;")
                
            status_label.setObjectName(f"status_{i}")
            status_label.setMinimumWidth(100)
            report_layout.addWidget(status_label)
            
            # Add the report frame to the vertical layout
            self.ui.reports_layout.addWidget(report_frame)
        
        # Add stretch at the end to push all reports to the top
        self.ui.reports_layout.addStretch()
    
    def prblm_clicked(self):
        """Handle when a report is selected."""
        # Only enable delete button if there are reports
        if self.prblm_lis:
            self.ui.delete_button.setEnabled(True)
    
    def get_selected_report_index(self):
        """
        Get the index of the selected report.
        
        Returns:
            int: The index of the selected report, or -1 if none selected
        """
        # Find which radio button is checked
        for i in range(len(self.prblm_lis)):
            radio_button = self.findChild(QtWidgets.QRadioButton, f"report_{i}")
            if radio_button and radio_button.isChecked():
                return i
        return -1
    
    def delete_clicked(self):
        """Handle when the Delete button is clicked."""
        selected_index = self.get_selected_report_index()
        if selected_index >= 0:
            # Confirm deletion
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setText("Are you sure you want to delete this report?")
            msg_box.setWindowTitle("Confirm Delete")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
            
            if msg_box.exec_() == QtWidgets.QMessageBox.Yes:
                # Get the report to be deleted
                report_to_delete = self.prblm_lis[selected_index]
                address_to_delete = report_to_delete[0]
                problem_to_delete = report_to_delete[1]
                
                # Remove the report from the list
                del self.prblm_lis[selected_index]
                
                # Update the userReports dictionary
                userReports[userAccount] = self.prblm_lis
                
                # Remove the report from the global reports list
                global reports
                reports_to_keep = []
                for report in reports:
                    # Check if this is the report to delete
                    if (report.get("username") == userAccount and 
                        report.get("address") == address_to_delete and 
                        report.get("problem") == problem_to_delete):
                        # Skip this report (don't add to reports_to_keep)
                        continue
                    # Keep all other reports
                    reports_to_keep.append(report)
                
                # Update the global reports list
                reports = reports_to_keep
                
                # Save the updated reports to file
                save_reports_to_file()
                
                # Refresh the display
                self.display_reports()
                
                # Disable delete button
                self.ui.delete_button.setEnabled(False)
    
    def back_clicked(self):
        """Handle when the Back button is clicked."""
        self.hide()
        self.next = MyMainScreen()
        self.next.showFullScreen()


class MyFaqScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global userAccount
        self.ui = FaqScreen.UI_FaqScreen()
        self.ui.setupUi(self)
        ui_utils.setup_modern_buttons(self)

        # Set window title and size
        self.setWindowTitle("Frequently Asked Questions")
        self.setMinimumSize(800, 600)

        # Apply modern styling to the FAQ content
        if hasattr(self.ui, "scrollArea"):
            self.ui.scrollArea.setStyleSheet(
                """
                QScrollArea {
                    background-color: #f5f5f5;
                    border: none;
                }
            """
            )

        # Style the FAQ title if it exists
        if hasattr(self.ui, "faq_title"):
            self.ui.faq_title.setStyleSheet(
                """
                QLabel {
                    color: #2c3e50;
                    font-size: 24px;
                    font-weight: bold;
                    margin-bottom: 20px;
                }
            """
            )

        # Style individual FAQ items
        question_labels = self.findChildren(QLabel, QRegExp("question_*"))
        for label in question_labels:
            label.setStyleSheet(
                """
                QLabel {
                    color: #2980b9;
                    font-size: 16px;
                    font-weight: bold;
                    padding: 10px 0;
                }
            """
            )

        answer_labels = self.findChildren(QLabel, QRegExp("answer_*"))
        for label in answer_labels:
            label.setStyleSheet(
                """
                QLabel {
                    color: #34495e;
                    font-size: 14px;
                    padding: 10px 0;
                }
            """
            )

        # Style frames if they exist
        frames = self.findChildren(QFrame, QRegExp("faq_frame_*"))
        for frame in frames:
            frame.setStyleSheet(
                """
                QFrame {
                    background-color: white;
                    border-radius: 8px;
                    border: 1px solid #e0e0e0;
                    margin: 10px;
                    padding: 15px;
                }
            """
            )

            # Add shadow effect to frames
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(10)
            shadow.setColor(QColor(0, 0, 0, 30))
            shadow.setOffset(0, 3)
            frame.setGraphicsEffect(shadow)

        # Style OK button
        if hasattr(self.ui, "ok_button"):
            self.ui.ok_button.setMinimumSize(150, 50)
            self.ui.ok_button.setCursor(Qt.PointingHandCursor)
            self.ui.ok_button.setStyleSheet(
                """
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border-radius: 5px;
                    font-size: 14px;
                    font-weight: bold;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """
            )

        self.ui.ok_button.clicked.connect(self.ok_clicked)

    def ok_clicked(self):
        if userAccount is not None:
            self.hide()
            self.next = MyMainScreen()
            self.next.showFullScreen()
        else:
            self.hide()
            self.next = MyFrontScreen()
            self.next.showFullScreen()

    def ok_clicked(self):
        self.hide()
        self.next = MyMainScreen()
        self.next.showFullScreen()


class MySuggestScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        print("MySuggestScreen initialized in main_ui.py") # Debugging message
        global userReports
        global suggestions
        global reports
        
        # Make a deep copy of the userReports dictionary to preserve it
        self.original_user_reports = {}
        for user, user_reports in userReports.items():
            self.original_user_reports[user] = user_reports.copy()

        # Convert the reports data from JSON file to the format expected by SuggestScreen
        reported_problems = []
        problem_id = 1

        # Use data from reports.json instead of test data
        load_reports_from_file()  # Make sure reports are loaded from file

        for report in reports:
            problem_data = {
                "id": problem_id,
                "address": report.get("address", "Unknown"),
                "problem_type": report.get("problem", "Unknown"),
                "description": report.get("description", "Unknown"),
                "date_reported": report.get(
                    "date", datetime.datetime.now().strftime("%Y-%m-%d")
                ),
            }
            reported_problems.append(problem_data)
            problem_id += 1

        # Use the updated SuggestScreen implementation
        self.suggest_screen = SuggestScreen.MySuggestScreen(self, reported_problems)
        
        # Connect the back button click to our custom method
        if hasattr(self.suggest_screen, 'ui') and hasattr(self.suggest_screen.ui, 'cancel_button'):
            self.suggest_screen.ui.cancel_button.clicked.disconnect()
            self.suggest_screen.ui.cancel_button.clicked.connect(self.back_to_main)
        
        # Set window flags to ensure it stays on top
        self.suggest_screen.setWindowFlags(self.suggest_screen.windowFlags() | Qt.WindowStaysOnTopHint)
        self.suggest_screen.showFullScreen()
        self.suggest_screen.activateWindow()  # Ensure it gets focus

    def back_to_main(self):
        """Handle navigation back to the main screen, ensuring reports data is preserved"""
        # Restore the original userReports dictionary
        global userReports
        userReports.clear()
        for user, user_reports in self.original_user_reports.items():
            userReports[user] = user_reports.copy()
            
        # Hide the suggest screen
        self.suggest_screen.hide()
        
        # Navigate back to the main screen
        self.next = MyMainScreen()
        self.next.showFullScreen()
        
        # Close this screen
        self.close()

    def cancel_clicked(self):
        # Restore the original userReports data before closing
        global userReports
        userReports.clear()
        for user, user_reports in self.original_user_reports.items():
            userReports[user] = user_reports.copy()
        self.close()

    def suggest_clicked(self, prblm):
        """Navigate to the SuggestScreen with the selected problem."""
        # Convert the tuple format to dictionary format expected by SuggestScreen
        problem_data = {
            "id": 0,
            "address": prblm[0],
            "problem_type": prblm[1],
            "description": f"Problem at {prblm[0]}",
            "date_reported": datetime.datetime.now().strftime("%Y-%m-%d"),
        }
        
        # Create a list with just this problem
        problem_list = [problem_data]
        
        # Create the suggestion screen with just this problem
        self.suggest_screen = SuggestScreen.MySuggestScreen(self, problem_list)
        
        # Connect the back button click to our custom method
        if hasattr(self.suggest_screen, 'ui') and hasattr(self.suggest_screen.ui, 'cancel_button'):
            self.suggest_screen.ui.cancel_button.clicked.disconnect()
            self.suggest_screen.ui.cancel_button.clicked.connect(self.back_to_main)
        
        # Hide current screen
        self.hide()
        
        # Set window flags to ensure it stays on top
        self.suggest_screen.setWindowFlags(self.suggest_screen.windowFlags() | Qt.WindowStaysOnTopHint)
        self.suggest_screen.showFullScreen()
        self.suggest_screen.activateWindow()  # Ensure it gets focus


class MyShare(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Share.Ui_Share()
        self.ui.setupUi(self)
        ui_utils.setup_modern_buttons(self)

        self.ui.pushButton.clicked.connect(self.send_clicked)

    def send_clicked(self):
        self.close()


class AdminReportViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        global reports

        # Configure the window
        self.setWindowTitle("Admin Report Management Dashboard")
        self.setMinimumSize(1000, 700)

        # Create central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        # Create header with shadow effect
        header_frame = QFrame(self)
        header_frame.setObjectName("headerFrame")
        header_frame.setStyleSheet(
            """
            #headerFrame {
                background-color: #ffffff;
                border-radius: 10px;
                padding: 10px;
            }
        """
        )
        header_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        header_frame.setMinimumHeight(100)
        header_frame.setMaximumHeight(120)
        header_layout = QVBoxLayout(header_frame)

        # Create header label
        self.header_label = QLabel("Toronto Reports Administration", self)
        self.header_label.setFont(QFont("Arial", 22, QFont.DemiBold))
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setStyleSheet("color: #2c3e50;")
        header_layout.addWidget(self.header_label)

        # Create admin status label
        self.admin_label = QLabel(
            "Administrator Dashboard - Full Access to All Reports", self
        )
        self.admin_label.setFont(QFont("Arial", 12, QFont.StyleItalic))
        self.admin_label.setStyleSheet("color: #3498db; margin-bottom: 10px;")
        self.admin_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(self.admin_label)

        # Apply drop shadow to header
        header_shadow = QGraphicsDropShadowEffect()
        header_shadow.setBlurRadius(15)
        header_shadow.setColor(QColor(0, 0, 0, 60))
        header_shadow.setOffset(0, 3)
        header_frame.setGraphicsEffect(header_shadow)

        # Add header to main layout
        self.main_layout.addWidget(header_frame)

        # Create dashboard metrics frame
        metrics_frame = QFrame(self)
        metrics_frame.setObjectName("metricsFrame")
        metrics_frame.setStyleSheet(
            """
            #metricsFrame {
                background-color: #ffffff;
                border-radius: 10px;
                padding: 10px;
            }
        """
        )
        metrics_layout = QHBoxLayout(metrics_frame)
        metrics_layout.setSpacing(20)

        # Apply metrics shadow
        metrics_shadow = QGraphicsDropShadowEffect()
        metrics_shadow.setBlurRadius(15)
        metrics_shadow.setColor(QColor(0, 0, 0, 60))
        metrics_shadow.setOffset(0, 3)
        metrics_frame.setGraphicsEffect(metrics_shadow)

        # Create metric cards
        self.total_reports_card = self.create_metric_card(
            "Total Reports", "0", "#3498db"
        )
        metrics_layout.addWidget(self.total_reports_card)

        self.active_users_card = self.create_metric_card("Active Users", "0", "#2ecc71")
        metrics_layout.addWidget(self.active_users_card)

        self.recent_reports_card = self.create_metric_card(
            "Reports This Week", "0", "#e74c3c"
        )
        metrics_layout.addWidget(self.recent_reports_card)

        # Add metrics frame to main layout
        self.main_layout.addWidget(metrics_frame)

        # Create main content frame
        content_frame = QFrame(self)
        content_frame.setObjectName("contentFrame")
        content_frame.setStyleSheet(
            """
            #contentFrame {
                background-color: #ffffff;
                border-radius: 10px;
                padding: 15px;
            }
        """
        )
        content_layout = QVBoxLayout(content_frame)

        # Apply content shadow
        content_shadow = QGraphicsDropShadowEffect()
        content_shadow.setBlurRadius(15)
        content_shadow.setColor(QColor(0, 0, 0, 60))
        content_shadow.setOffset(0, 3)
        content_frame.setGraphicsEffect(content_shadow)

        # Create search and filter layout
        search_layout = QHBoxLayout()

        # Search box
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search reports...")
        self.search_input.setMinimumHeight(40)
        self.search_input.setStyleSheet(
            """
            QLineEdit {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 5px 10px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
        """
        )
        self.search_input.textChanged.connect(self.filter_reports)
        search_layout.addWidget(self.search_input, 3)

        # Filter combobox
        self.filter_combo = QComboBox(self)
        self.filter_combo.addItems(
            [
                "All Problems",
                "Utility Failures",
                "Potholes",
                "Vandalism",
                "Eroded Streets",
                "Tree Collapse",
                "Flooded Streets",
                "Mold and Spore Growth",
                "Garbage or any Other Road Blocking Objects",
            ]
        )
        self.filter_combo.setMinimumHeight(40)
        self.filter_combo.setStyleSheet(
            """
            QComboBox {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 5px 10px;
                font-size: 14px;
            }
            QComboBox:hover {
                border: 1px solid #3498db;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: #bdc3c7;
                border-left-style: solid;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
            }
        """
        )
        self.filter_combo.currentIndexChanged.connect(self.filter_reports)
        search_layout.addWidget(self.filter_combo, 1)

        # Add search and filter layout to content
        content_layout.addLayout(search_layout)

        # Create table widget for reports with modern styling
        self.reports_table = QTableWidget(self)
        self.reports_table.setColumnCount(6)
        self.reports_table.setHorizontalHeaderLabels(
            ["Date", "Username", "Address", "Problem Type", "Status", "Description"]
        )
        self.reports_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.reports_table.setAlternatingRowColors(True)
        self.reports_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.reports_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.reports_table.setStyleSheet(
            """
            QTableWidget {
                border: 1px solid #e0e0e0;
                border-radius: 5px;
                font-size: 14px;
            }
            QTableWidget::item {
                padding: 10px;
                border-bottom: 1px solid #e0e0e0;
            }
            QTableWidget::item:selected {
                background-color: #e0f2fe;
                color: #2c3e50;
            }
            QHeaderView::section {
                background-color: #3498db;
                color: white;
                padding: 12px;
                font-weight: bold;
                border: none;
            }
            QTableWidget::item:alternate {
                background-color: #f8f9fa;
            }
        """
        )

        # Connect double-click to view details
        self.reports_table.doubleClicked.connect(self.view_report_details)

        # Add table to content layout
        content_layout.addWidget(self.reports_table)

        # Add content frame to main layout
        self.main_layout.addWidget(content_frame)

        # Create button layout
        self.button_layout = QHBoxLayout()

        # Create action buttons with icons
        self.refresh_button = self.create_action_button(
            "Refresh", "Reload reports from data file", self.load_reports
        )
        self.button_layout.addWidget(self.refresh_button)

        self.view_button = self.create_action_button(
            "View Details", "View selected report details", self.view_report_details
        )
        self.button_layout.addWidget(self.view_button)

        self.export_button = self.create_action_button(
            "Export CSV", "Export reports to CSV file", self.export_to_csv
        )
        self.button_layout.addWidget(self.export_button)

        self.status_button = self.create_action_button(
            "Update Status", "Update the status of the selected report", self.update_status
        )
        self.button_layout.addWidget(self.status_button)

        self.back_button = self.create_action_button(
            "Back to Main", "Return to main screen", self.go_back
        )
        self.button_layout.addWidget(self.back_button)

        # Add button layout to main layout
        self.main_layout.addLayout(self.button_layout)

        # Set main window style
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #f0f2f5;
            }
        """
        )

        # Initialize data
        self.load_reports()

        # Debug message
        print("AdminReportViewer initialized with modern UI")

    def create_metric_card(self, title, value, color):
        """Create a metric card widget for the dashboard"""
        card = QFrame()
        card.setObjectName("metricCard")
        card.setStyleSheet(
            f"""
            #metricCard {{
                border-radius: 10px;
                border-left: 6px solid {color};
                background-color: white;
                padding: 15px;
            }}
        """
        )

        layout = QVBoxLayout(card)

        # Card title
        title_label = QLabel(title, card)
        title_label.setStyleSheet(
            f"color: {color}; font-weight: bold; font-size: 14px;"
        )
        layout.addWidget(title_label)

        # Card value
        value_label = QLabel(value, card)
        value_label.setObjectName(f"{title.lower().replace(' ', '_')}_value")
        value_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(value_label)

        return card

    def create_action_button(self, text, tooltip, callback):
        """Create styled action button"""
        button = QPushButton(text, self)
        button.setToolTip(tooltip)
        button.setMinimumSize(130, 45)
        button.setCursor(Qt.PointingHandCursor)
        button.clicked.connect(callback)
        button.setStyleSheet(
            """
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 5px;
                padding: 10px 15px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c6ea4;
            }
        """
        )
        return button

    def load_reports(self):
        """Load all reports from JSON file into the table"""
        global reports

        # Make sure reports are loaded from file
        load_reports_from_file()

        # Clear the table first
        self.reports_table.setRowCount(0)

        # Filter reports based on current filter
        filtered_reports = self.get_filtered_reports()

        # Update metrics
        self.update_metrics(reports)

        # Add each report to the table
        for i, report in enumerate(filtered_reports):
            self.reports_table.insertRow(i)

            # Create items for each column
            date_item = QTableWidgetItem(report.get("date", "Unknown"))
            username_item = QTableWidgetItem(report.get("username", "Unknown"))
            address_item = QTableWidgetItem(report.get("address", "Unknown"))
            problem_item = QTableWidgetItem(report.get("problem", "Unknown"))

            # Get status or set default to "Pending"
            status = report.get("status", "Pending")
            status_item = QTableWidgetItem(status)
            
            # Set status color based on value
            if status == "Pending":
                status_item.setForeground(QColor("#f39c12"))  # Orange
            elif status == "In Progress":
                status_item.setForeground(QColor("#3498db"))  # Blue
            elif status == "Resolved":
                status_item.setForeground(QColor("#27ae60"))  # Green
            elif status == "Closed":
                status_item.setForeground(QColor("#7f8c8d"))  # Gray
            
            # Make status bold
            font = status_item.font()
            font.setBold(True)
            status_item.setFont(font)

            # Truncate description if it's too long
            description = report.get("description", "Unknown")
            if len(description) > 50:
                description = description[:47] + "..."
            description_item = QTableWidgetItem(description)

            # Add items to the table
            self.reports_table.setItem(i, 0, date_item)
            self.reports_table.setItem(i, 1, username_item)
            self.reports_table.setItem(i, 2, address_item)
            self.reports_table.setItem(i, 3, problem_item)
            self.reports_table.setItem(i, 4, status_item)
            self.reports_table.setItem(i, 5, description_item)

        # Auto adjust row heights for better readability
        self.reports_table.resizeRowsToContents()

        print(f"Loaded {len(filtered_reports)} reports into admin view")

    def update_metrics(self, reports):
        """Update the metrics displayed in the dashboard"""
        # Total reports count
        total_reports = len(reports)
        self.total_reports_card.findChild(QLabel, "total_reports_value").setText(
            str(total_reports)
        )

        # Count unique users
        unique_users = set()
        recent_reports = 0

        # Check for reports in the last week
        today = datetime.datetime.now()
        one_week_ago = today - datetime.timedelta(days=7)

        for report in reports:
            username = report.get("username")
            if username:
                unique_users.add(username)

            # Count recent reports (within the last week)
            try:
                report_date = datetime.datetime.strptime(
                    report.get("date", ""), "%Y-%m-%d"
                )
                if report_date >= one_week_ago:
                    recent_reports += 1
            except:
                pass

        # Update metrics
        self.active_users_card.findChild(QLabel, "active_users_value").setText(
            str(len(unique_users))
        )
        self.recent_reports_card.findChild(QLabel, "reports_this_week_value").setText(
            str(recent_reports)
        )

    def get_filtered_reports(self):
        """Get reports based on current filter and search text"""
        global reports

        search_text = (
            self.search_input.text().lower() if hasattr(self, "search_input") else ""
        )
        problem_filter = (
            self.filter_combo.currentText()
            if hasattr(self, "filter_combo")
            else "All Problems"
        )

        filtered_reports = []

        for report in reports:
            # Apply problem type filter
            if (
                problem_filter != "All Problems"
                and report.get("problem") != problem_filter
            ):
                continue

            # Apply text search
            if search_text:
                report_text = (
                    str(report.get("username", "")).lower()
                    + " "
                    + str(report.get("address", "")).lower()
                    + " "
                    + str(report.get("problem", "")).lower()
                    + " "
                    + str(report.get("description", "")).lower()
                )
                if search_text not in report_text:
                    continue

            filtered_reports.append(report)

        return filtered_reports

    def filter_reports(self):
        """Apply filtering and reload the table"""
        # Reload reports with current filter
        self.load_reports()

    def view_report_details(self):
        """View detailed information about the selected report"""
        selected_items = self.reports_table.selectedItems()

        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select a report to view.")
            return

        row = selected_items[0].row()
        filtered_reports = self.get_filtered_reports()

        if row >= 0 and row < len(filtered_reports):
            report = filtered_reports[row]

            # Create a styled detail dialog
            dialog = QDialog(self)
            dialog.setWindowTitle("Report Details")
            dialog.setMinimumSize(700, 500)
            dialog.setStyleSheet(
                """
                QDialog {
                    background-color: #f0f2f5;
                }
                QLabel {
                    font-size: 14px;
                }
                QLabel[heading="true"] {
                    font-weight: bold;
                    color: #2c3e50;
                    font-size: 16px;
                }
            """
            )

            # Dialog layout
            layout = QVBoxLayout(dialog)
            layout.setContentsMargins(20, 20, 20, 20)
            layout.setSpacing(15)

            # Create header
            header = QLabel("Detailed Report Information", dialog)
            header.setStyleSheet(
                "font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;"
            )
            header.setAlignment(Qt.AlignCenter)
            layout.addWidget(header)

            # Create content frame
            content_frame = QFrame(dialog)
            content_frame.setObjectName("detailsFrame")
            content_frame.setStyleSheet(
                """
                #detailsFrame {
                    background-color: white;
                    border-radius: 10px;
                    padding: 20px;
                }
            """
            )
            content_layout = QFormLayout(content_frame)
            content_layout.setRowWrapPolicy(QFormLayout.WrapAllRows)
            content_layout.setLabelAlignment(Qt.AlignRight)
            content_layout.setFormAlignment(Qt.AlignLeft)
            content_layout.setSpacing(15)

            # Add report fields with styled labels
            date_label = QLabel(report.get("date", "Unknown"), content_frame)
            date_heading = QLabel("Date:", content_frame)
            date_heading.setProperty("heading", "true")
            content_layout.addRow(date_heading, date_label)

            username_label = QLabel(report.get("username", "Unknown"), content_frame)
            username_heading = QLabel("Username:", content_frame)
            username_heading.setProperty("heading", "true")
            content_layout.addRow(username_heading, username_label)

            address_label = QLabel(report.get("address", "Unknown"), content_frame)
            address_label.setWordWrap(True)
            address_heading = QLabel("Address:", content_frame)
            address_heading.setProperty("heading", "true")
            content_layout.addRow(address_heading, address_label)

            problem_label = QLabel(report.get("problem", "Unknown"), content_frame)
            problem_heading = QLabel("Problem:", content_frame)
            problem_heading.setProperty("heading", "true")
            content_layout.addRow(problem_heading, problem_label)

            # Create separator
            separator = QFrame(content_frame)
            separator.setFrameShape(QFrame.HLine)
            separator.setFrameShadow(QFrame.Sunken)
            separator.setStyleSheet("background-color: #e0e0e0;")
            content_layout.addRow(separator)

            # Description heading
            desc_heading = QLabel("Description:", content_frame)
            desc_heading.setProperty("heading", "true")
            content_layout.addRow(desc_heading)

            # Add description text browser
            description_browser = QTextBrowser(content_frame)
            description_browser.setText(report.get("description", "Unknown"))
            description_browser.setMinimumHeight(150)
            description_browser.setStyleSheet(
                """
                QTextBrowser {
                    border: 1px solid #e0e0e0;
                    border-radius: 5px;
                    padding: 10px;
                    background-color: #f9f9f9;
                    font-size: 14px;
                }
            """
            )
            content_layout.addRow(description_browser)

            # Apply shadow to content frame
            content_shadow = QGraphicsDropShadowEffect()
            content_shadow.setBlurRadius(20)
            content_shadow.setColor(QColor(0, 0, 0, 50))
            content_shadow.setOffset(0, 5)
            content_frame.setGraphicsEffect(content_shadow)

            # Add content frame to dialog
            layout.addWidget(content_frame)

            # Create buttons layout
            buttons_layout = QHBoxLayout()

            # Map button
            map_button = QPushButton("Show on Map", dialog)
            map_button.setMinimumHeight(45)
            map_button.setCursor(Qt.PointingHandCursor)
            map_button.setStyleSheet(
                """
                QPushButton {
                    background-color: #27ae60;
                    color: white;
                    border-radius: 5px;
                    padding: 10px 20px;
                    font-weight: bold;
                    font-size: 16px;
                    min-width: 150px;
                }
                QPushButton:hover {
                    background-color: #219a52;
                }
            """
            )
            map_button.clicked.connect(lambda: self.show_report_on_map(report))
            buttons_layout.addWidget(map_button)

            # Close button
            close_button = QPushButton("Close", dialog)
            close_button.clicked.connect(dialog.accept)
            close_button.setMinimumHeight(45)
            close_button.setCursor(Qt.PointingHandCursor)
            close_button.setStyleSheet(
                """
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border-radius: 5px;
                    padding: 10px 20px;
                    font-weight: bold;
                    font-size: 16px;
                    min-width: 150px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """
            )
            buttons_layout.addWidget(close_button)

            # Add buttons layout to dialog
            layout.addLayout(buttons_layout)

            # Show the dialog
            dialog.exec_()

    def show_report_on_map(self, report):
        """Show the selected report location on a map"""
        address = report.get("address", "")
        if address:
            try:
                # Create and show the map dialog with the report address
                from MapDialog import MapDialog

                map_dialog = MapDialog(self)
                map_dialog.load_map(address)
                map_dialog.exec_()
            except Exception as e:
                QMessageBox.warning(
                    self, "Map Error", f"Could not display map: {str(e)}"
                )
        else:
            QMessageBox.warning(
                self, "Location Error", "No address available for this report."
            )

    def export_to_csv(self):
        """Export reports to a CSV file"""
        try:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(
                self, "Export Reports", "", "CSV Files (*.csv)"
            )

            if file_path:
                # Get filtered reports
                filtered_reports = self.get_filtered_reports()

                with open(file_path, "w", newline="") as csv_file:
                    import csv

                    writer = csv.writer(csv_file)

                    # Write header
                    writer.writerow(
                        ["Date", "Username", "Address", "Problem", "Status", "Description"]
                    )

                    # Write data
                    for report in filtered_reports:
                        writer.writerow(
                            [
                                report.get("date", "Unknown"),
                                report.get("username", "Unknown"),
                                report.get("address", "Unknown"),
                                report.get("problem", "Unknown"),
                                report.get("status", "Unknown"),
                                report.get("description", "Unknown"),
                            ]
                        )

                QMessageBox.information(
                    self,
                    "Export Successful",
                    f"Reports exported successfully to {file_path}",
                )
        except Exception as e:
            QMessageBox.critical(
                self, "Export Error", f"Error exporting reports: {str(e)}"
            )

    def go_back(self):
        """Return to the main screen"""
        self.hide()
        self.next = MyMainScreen()
        self.next.showFullScreen()

    def update_status(self):
        """Update the status of the selected report"""
        selected_items = self.reports_table.selectedItems()

        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select a report to update.")
            return

        row = selected_items[0].row()
        filtered_reports = self.get_filtered_reports()

        if row >= 0 and row < len(filtered_reports):
            report = filtered_reports[row]

            # Create a styled status dialog
            dialog = QDialog(self)
            dialog.setWindowTitle("Update Report Status")
            dialog.setMinimumSize(400, 200)
            dialog.setStyleSheet(
                """
                QDialog {
                    background-color: #f0f2f5;
                }
                QLabel {
                    font-size: 14px;
                }
                QLabel[heading="true"] {
                    font-weight: bold;
                    color: #2c3e50;
                    font-size: 16px;
                }
            """
            )

            # Dialog layout
            layout = QVBoxLayout(dialog)
            layout.setContentsMargins(20, 20, 20, 20)
            layout.setSpacing(15)

            # Create header
            header = QLabel("Update Report Status", dialog)
            header.setStyleSheet(
                "font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;"
            )
            header.setAlignment(Qt.AlignCenter)
            layout.addWidget(header)

            # Create status combo box
            status_combo = QComboBox(dialog)
            status_combo.addItems(["Pending", "In Progress", "Resolved", "Closed"])
            status_combo.setCurrentText(report.get("status", "Pending"))
            layout.addWidget(status_combo)

            # Create buttons layout
            buttons_layout = QHBoxLayout()

            # Update button
            update_button = QPushButton("Update", dialog)
            update_button.clicked.connect(lambda: self.update_report_status(dialog, report, status_combo))
            update_button.setMinimumHeight(45)
            update_button.setCursor(Qt.PointingHandCursor)
            update_button.setStyleSheet(
                """
                QPushButton {
                    background-color: #27ae60;
                    color: white;
                    border-radius: 5px;
                    padding: 10px 20px;
                    font-weight: bold;
                    font-size: 16px;
                    min-width: 150px;
                }
                QPushButton:hover {
                    background-color: #219a52;
                }
            """
            )
            buttons_layout.addWidget(update_button)

            # Close button
            close_button = QPushButton("Close", dialog)
            close_button.clicked.connect(dialog.accept)
            close_button.setMinimumHeight(45)
            close_button.setCursor(Qt.PointingHandCursor)
            close_button.setStyleSheet(
                """
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border-radius: 5px;
                    padding: 10px 20px;
                    font-weight: bold;
                    font-size: 16px;
                    min-width: 150px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """
            )
            buttons_layout.addWidget(close_button)

            # Add buttons layout to dialog
            layout.addLayout(buttons_layout)

            # Show the dialog
            dialog.exec_()

    def update_report_status(self, dialog, report, status_combo):
        """Update the report status"""
        new_status = status_combo.currentText()
        report["status"] = new_status

        # Save the updated reports to file
        save_reports_to_file()

        # Reload the reports table
        self.load_reports()

        # Close the dialog
        dialog.accept()


def save_reports_to_file():
    global reports
    try:
        with open("reports.json", "w") as file:
            json.dump(reports, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving reports: {str(e)}")
        return False


def load_reports_from_file():
    global reports, userReports
    try:
        if os.path.exists("reports.json"):
            with open("reports.json", "r") as file:
                loaded_reports = json.load(file)
                reports = loaded_reports
                
                # Create a temporary dictionary to store reports by username
                temp_reports = {}
                
                # First pass: collect all reports by username
                for report in reports:
                    username = report.get("username")
                    if username:
                        if username not in temp_reports:
                            temp_reports[username] = []
                        
                        # Create report entry in the format expected by MyUserReports
                        report_entry = [report.get("address"), report.get("problem"), report.get("status")]
                        
                        # Only add the report if it's not already in the list
                        if report_entry not in temp_reports[username]:
                            temp_reports[username].append(report_entry)
                
                # Second pass: update userReports with the collected reports
                for username, user_reports in temp_reports.items():
                    if username not in userReports:
                        userReports[username] = []
                    
                    # Add any reports that aren't already in userReports
                    for report_entry in user_reports:
                        if report_entry not in userReports[username]:
                            userReports[username].append(report_entry)
                            
    except Exception as e:
        print(f"Error loading reports: {str(e)}")


def is_duplicate_report(address, problem_type):
    """
    Check if a report with the same address and problem type already exists.
    
    Args:
        address (str): The address of the report
        problem_type (str): The type of problem being reported
        
    Returns:
        bool: True if a duplicate exists, False otherwise
    """
    global reports
    
    # Normalize inputs for comparison
    address = address.strip().lower()
    problem_type = problem_type.strip().lower()
    
    for report in reports:
        # Compare normalized address and problem type
        if (report["address"].strip().lower() == address and 
            report["problem"].strip().lower() == problem_type):
            return True
    
    return False

load_reports_from_file()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_utils.apply_stylesheet(app)
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    w = MyFrontScreen()
    w.showFullScreen()  # Open in maximized window instead of normal size
    sys.exit(app.exec_())
