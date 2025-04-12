#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Report Screen Module

This module provides the UI for submitting reports about city issues.
It allows citizens to enter an address, select a problem type,
and provide additional details about issues they encounter.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from MapDialog import MapDialog
import os
import json
from main_ui import is_duplicate_report, active_user
from bot_detection import verify_human_user, get_reputation_system
from report_validator import verify_report_legitimacy
import datetime

class Ui_ReportScreen(object):
    """
    UI class for the Report Screen.
    
    This class defines the user interface elements for the report submission screen,
    allowing users to report various city issues with location details.
    """
    
    def setupUi(self, ReportScreen):
        """
        Set up the user interface for the Report Screen.
        
        Args:
            ReportScreen (QMainWindow): The main window to set up
        """
        ReportScreen.setObjectName("ReportScreen")
        ReportScreen.resize(900, 700)
        ReportScreen.setWindowIcon(QtGui.QIcon('images/cypress_logo.png'))
        ReportScreen.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(ReportScreen)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create main layout
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(40, 40, 40, 40)
        self.mainLayout.setSpacing(30)
        self.mainLayout.setObjectName("mainLayout")
        
        # Create title label
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setText("Report an Issue")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.mainLayout.addWidget(self.title_label)
        
        # Create content widget with box shadow
        self.content_widget = QtWidgets.QWidget(self.centralwidget)
        self.content_widget.setObjectName("content_widget")
        self.content_widget.setStyleSheet("""
            #content_widget {
                background-color: white;
                border-radius: 10px;
            }
        """)
        
        # Create content layout
        self.content_layout = QtWidgets.QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(30, 30, 30, 30)
        self.content_layout.setSpacing(25)
        self.content_layout.setObjectName("content_layout")
        
        self._setup_address_section()
        self._setup_problems_section()
        self._setup_description_section()
        self._setup_attachment_section()  # Maintain compatibility with main_ui.py
        self._setup_buttons()
        
        self.mainLayout.addWidget(self.content_widget)
        ReportScreen.setCentralWidget(self.centralwidget)
        
        # Add statusbar for backward compatibility
        self.statusbar = QtWidgets.QStatusBar(ReportScreen)
        self.statusbar.setObjectName("statusbar")
        ReportScreen.setStatusBar(self.statusbar)
        
        self.set_text(ReportScreen)
        QtCore.QMetaObject.connectSlotsByName(ReportScreen)
    
    def _setup_address_section(self):
        """Set up the address input section of the form."""
        # Create form layout for address
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setSpacing(10)
        self.form_layout.setObjectName("form_layout")
        self.form_layout.setLabelAlignment(QtCore.Qt.AlignRight)
        self.form_layout.setFormAlignment(QtCore.Qt.AlignLeft)
        
        # Address input with layout
        address_layout = QtWidgets.QHBoxLayout()
        self.address_input = QtWidgets.QLineEdit(self.content_widget)
        self.address_input.setMinimumHeight(40)
        # Increase width to prevent text cutoff
        self.address_input.setMinimumWidth(400)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.address_input.setFont(font)
        self.address_input.setPlaceholderText("Enter the location of the issue")
        self.address_input.setObjectName("address_input")
        
        # Add map button with red location marker icon
        self.map_button = QtWidgets.QPushButton(self.content_widget)
        self.map_button.setObjectName("map_button")
        
        # Use the SVG file for the map marker icon
        icon_path = "icons/location-marker-red.svg"
        if os.path.exists(icon_path):
            # Create a QIcon from the SVG file
            icon = QtGui.QIcon(icon_path)
            self.map_button.setIcon(icon)
        else:
            # Fallback to the original icon if the SVG is missing
            self.map_button.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/map-pin.png")))
            
        self.map_button.setIconSize(QtCore.QSize(32, 32))
        self.map_button.setToolTip("Select location on map")
        self.map_button.setFixedSize(48, 48)
        self.map_button.setStyleSheet("""
            QPushButton {
                background-color: #f8f9fa;
                border: 1px solid #ddd;
                border-radius: 24px;
                padding: 4px;
            }
            QPushButton:hover {
                background-color: #e9ecef;
            }
        """)
        
        # Add address input and map button to the layout
        address_layout.addWidget(self.address_input)
        address_layout.addWidget(self.map_button)
        
        self.address_label = QtWidgets.QLabel(self.content_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.address_label.setFont(font)
        self.address_label.setObjectName("address_label")
        self.form_layout.addRow(self.address_label, address_layout)
        self.content_layout.addLayout(self.form_layout)
    
    def _setup_problems_section(self):
        """Set up the problem selection section of the form."""
        # Problems label
        self.problems_label = QtWidgets.QLabel(self.content_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.problems_label.setFont(font)
        self.problems_label.setObjectName("problems_label")
        self.content_layout.addWidget(self.problems_label)
        
        # Problem selection area
        self.problems_card = QtWidgets.QFrame(self.content_widget)
        self.problems_card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.problems_card.setFrameShadow(QtWidgets.QFrame.Raised)
        self.problems_card.setObjectName("problems_card")
        self.problems_card.setStyleSheet("""
            #problems_card {
                background-color: #f8f9fa;
                border-radius: 8px;
            }
        """)
        
        self.problems_layout = QtWidgets.QGridLayout(self.problems_card)
        self.problems_layout.setContentsMargins(20, 20, 20, 20)
        self.problems_layout.setSpacing(15)
        self.problems_layout.setObjectName("problems_layout")
        
        # Create radio buttons for problems
        self.problems_group = QtWidgets.QButtonGroup(self.problems_card)
        self.problems_group.setObjectName("problems_group")
        
        # Create problem radio buttons
        self._create_problem_buttons()
        
        self.content_layout.addWidget(self.problems_card)
    
    def _create_problem_buttons(self):
        """Create the radio buttons for different problem types."""
        font = QtGui.QFont()
        font.setPointSize(11)
        
        # Define problem types and their positions
        problem_types = [
            # Left column
            ("utility_failures_button", 0, 0),
            ("potholes_button", 1, 0),
            ("vandalism_button", 2, 0),
            ("erroded_streets_button", 3, 0),
            
            # Right column
            ("tree_collapse_button", 0, 1),
            ("flooded_streets_button", 1, 1),
            ("mould_button", 2, 1),
            ("garbage_button", 3, 1)
        ]
        
        # Create each button
        for button_name, row, col in problem_types:
            button = QtWidgets.QRadioButton(self.problems_card)
            button.setFont(font)
            button.setObjectName(button_name)
            self.problems_layout.addWidget(button, row, col)
            self.problems_group.addButton(button)
            
            # Store the button as an instance attribute
            setattr(self, button_name, button)
    
    def _setup_description_section(self):
        """Set up the description input section of the form."""
        # Description section
        self.description_label = QtWidgets.QLabel(self.content_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.description_label.setFont(font)
        self.description_label.setObjectName("description_label")
        self.content_layout.addWidget(self.description_label)
        
        self.description_input = QtWidgets.QTextEdit(self.content_widget)
        # Increase minimum height to show more text and prevent cutoff
        self.description_input.setMinimumHeight(180)
        # Set word wrap mode to ensure text wraps properly
        self.description_input.setWordWrapMode(QtGui.QTextOption.WordWrap)
        # Increase line height for better readability
        document = self.description_input.document()
        document.setDocumentMargin(10)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.description_input.setFont(font)
        self.description_input.setPlaceholderText("Provide additional details about the issue...")
        self.description_input.setObjectName("description_input")
        # Add custom style to make text more readable
        self.description_input.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 10px;
                line-height: 1.5;
            }
        """)
        self.content_layout.addWidget(self.description_input)

    def _setup_attachment_section(self):
        """Set up the attachment section (for backward compatibility with main_ui.py)."""
        # Attachment section
        self.attachment_label = QtWidgets.QLabel(self.content_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.attachment_label.setFont(font)
        self.attachment_label.setObjectName("attachment_label")
        self.content_layout.addWidget(self.attachment_label)
        
        # Attachment widgets container
        self.attachment_container = QtWidgets.QWidget(self.content_widget)
        self.attachment_container.setObjectName("attachment_container")
        self.attachment_layout = QtWidgets.QHBoxLayout(self.attachment_container)
        self.attachment_layout.setContentsMargins(0, 0, 0, 0)
        self.attachment_layout.setSpacing(15)
        
        # Drop area for attachments
        self.drop_area = QtWidgets.QLabel(self.attachment_container)
        self.drop_area.setMinimumSize(QtCore.QSize(200, 120))
        self.drop_area.setMaximumSize(QtCore.QSize(200, 120))
        self.drop_area.setAlignment(QtCore.Qt.AlignCenter)
        self.drop_area.setStyleSheet("""
            QLabel {
                border: 2px dashed #aaaaaa;
                border-radius: 5px;
                background-color: #f8f9fa;
                color: #666666;
            }
        """)
        self.drop_area.setText("Drag & Drop Image\nor Click to Browse")
        self.drop_area.setWordWrap(True)
        self.drop_area.setObjectName("drop_area")
        self.attachment_layout.addWidget(self.drop_area)
        
        # Browse button
        self.browse_button = QtWidgets.QPushButton(self.attachment_container)
        self.browse_button.setMinimumSize(QtCore.QSize(150, 40))
        self.browse_button.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.browse_button.setFont(font)
        self.browse_button.setObjectName("browse_button")
        self.attachment_layout.addWidget(self.browse_button)
        
        # Add stretch to push elements to the left
        self.attachment_layout.addStretch()
        
        # Add attachment container to content layout
        self.content_layout.addWidget(self.attachment_container)
    
    def _setup_buttons(self):
        """Set up the submit and cancel buttons."""
        # Create button container with centered layout
        self.button_container = QtWidgets.QWidget(self.content_widget)
        self.button_container.setObjectName("button_container")
        
        # Create horizontal layout for buttons and center them
        self.button_layout = QtWidgets.QHBoxLayout(self.button_container)
        self.button_layout.setContentsMargins(0, 10, 0, 0)
        self.button_layout.setSpacing(20)
        self.button_layout.setAlignment(QtCore.Qt.AlignCenter)  # Center the buttons
        
        # Report button
        self.report_button = QtWidgets.QPushButton(self.button_container)
        self.report_button.setMinimumSize(QtCore.QSize(200, 50))
        self.report_button.setObjectName("report_button")
        self.report_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f6dad;
            }
        """)
        self.button_layout.addWidget(self.report_button)
        
        # Cancel button
        self.cancel_button = QtWidgets.QPushButton(self.button_container)
        self.cancel_button.setMinimumSize(QtCore.QSize(200, 50))
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #a93226;
            }
        """)
        self.button_layout.addWidget(self.cancel_button)
        
        # Add button container to content layout
        self.content_layout.addWidget(self.button_container)
        
        # Create submit_button as an alias to report_button for new code
        self.submit_button = self.report_button
    
    def set_text(self, ReportScreen):
        """
        Set the text for UI elements.
        
        Args:
            ReportScreen (QMainWindow): The main window containing the UI elements
        """
        # Set window title and labels directly without translation
        ReportScreen.setWindowTitle("Report an Issue")
        self.address_label.setText("Address:")
        self.problems_label.setText("What's the problem?")
        
        # Problem options - match with global allProblems list from main_ui.py
        self.utility_failures_button.setText("Water/Electricity Outage")
        self.potholes_button.setText("Road Damage (Potholes)")
        self.vandalism_button.setText("Graffiti and Vandalism")
        self.erroded_streets_button.setText("Street Erosion")
        self.tree_collapse_button.setText("Fallen Trees/Branches")
        self.flooded_streets_button.setText("Street Flooding")
        self.mould_button.setText("Public Health Hazard")
        self.garbage_button.setText("Roadway Obstruction")
        
        # Set other UI text directly
        self.description_label.setText("Description")
        self.attachment_label.setText("Attach Image:")
        self.browse_button.setText("Browse Files")
        self.cancel_button.setText("Back")
        self.report_button.setText("Report")

class MyReportScreen(QtWidgets.QMainWindow, Ui_ReportScreen):
    """
    Functional implementation of the Report Screen.
    
    This class extends the UI definition with actual functionality, handling
    user interactions and connecting signals to slots.
    """
    
    def __init__(self, parent=None, edit_mode=False, report_data=None, report_id=None):
        """
        Initialize the Report Screen with functionality.
        
        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
            edit_mode (bool, optional): Whether this screen is in edit mode. Defaults to False.
            report_data (dict, optional): Report data to edit. Required if edit_mode is True.
            report_id (int, optional): ID of the report being edited. Required if edit_mode is True.
        """
        super(MyReportScreen, self).__init__(parent)
        self.setupUi(self)
        
        # Store edit mode parameters
        self.edit_mode = edit_mode
        self.report_data = report_data
        self.report_id = report_id
        self.parent_screen = parent
        
        # Update UI based on mode
        if edit_mode:
            self.title_label.setText("Edit Report")
            self.submit_button.setText("Update Report")
            
            # Load the report data into the form
            if report_data:
                # Set address
                self.address_input.setText(report_data.get("location", ""))
                
                # Set problem type
                problem_type = report_data.get("type", "")
                problem_button_map = {
                    "Pothole": "potholes_button",
                    "Road Damage (Potholes)": "potholes_button",
                    "Street Light Out": "utility_failures_button",
                    "Water/Electricity Outage": "utility_failures_button",
                    "Utility Failures": "utility_failures_button",
                    "Graffiti": "vandalism_button",
                    "Graffiti and Vandalism": "vandalism_button",
                    "Street Erosion": "erroded_streets_button",
                    "Tree Collapse": "tree_collapse_button",
                    "Fallen Trees/Branches": "tree_collapse_button",
                    "Flooded Streets": "flooded_streets_button",
                    "Street Flooding": "flooded_streets_button",
                    "Public Health Hazard": "mould_button",
                    "Roadway Obstruction": "garbage_button"
                }
                
                # Try to find the matching button
                button_name = problem_button_map.get(problem_type)
                if button_name and hasattr(self, button_name):
                    button = getattr(self, button_name)
                    button.setChecked(True)
                
                # Set description
                self.description_input.setPlainText(report_data.get("description", ""))
                
                print(f"Successfully loaded report data for editing: {report_data}")
        
        # Connect signals to slots
        self.cancel_button.clicked.connect(self.cancel_clicked)
        self.submit_button.clicked.connect(self.submit_report)
        self.map_button.clicked.connect(self.open_map_dialog)
    
    def submit_report(self):
        """Handle the submission of a report or update of an existing report."""
        # Validate inputs
        if not self.validate_inputs():
            return
        
        # Get input values
        address = self.address_input.text().strip()
        problem = self.get_selected_problem()
        description = self.description_input.toPlainText().strip()
        
        # Current time for report
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Create report data for validation
        report_data = {
            "location": address,
            "type": problem,
            "description": description,
            "date": formatted_time,
            "username": active_user,
            "status": "Submitted"
        }
        
        # Get reputation system instance
        reputation_system = get_reputation_system()
        print(f"Using reputation system instance: {id(reputation_system)}")
        
        # Check if user is already flagged
        if reputation_system.is_user_flagged(active_user):
            QtWidgets.QMessageBox.warning(
                self,
                "Account Restricted",
                "Your account has been flagged for suspicious activity. "
                "You cannot submit reports at this time. Please contact an administrator."
            )
            return
            
        # Always show CAPTCHA for rapid submissions
        # Verify human user before proceeding (bot detection)
        if not verify_human_user(self, active_user):
            # Verification failed, don't submit the report
            reputation_system.log_captcha_failure(active_user)
            return
        
        # Verify report legitimacy to catch suspicious patterns
        if not verify_report_legitimacy(report_data, active_user, self):
            # Report failed legitimacy check
            # The function will already show a warning to the user
            reputation_system.log_report_submission(active_user, is_valid=False)
            return
        
        # Check for rapid submissions - get user data
        reputation = reputation_system.get_user_reputation(active_user)
        print(f"Current reputation for {active_user}: {reputation}")
        
        # If user has submitted a report recently (within 1 minute)
        if reputation['last_report_time']:
            try:
                # Parse the timestamp string into a datetime object
                last_time = datetime.datetime.fromisoformat(reputation['last_report_time'])
                time_diff_seconds = (current_time - last_time).total_seconds()
                print(f"Time since last report: {time_diff_seconds} seconds")
                
                # If submissions are too rapid (less than 30 seconds apart)
                if time_diff_seconds < 30:
                    # Penalize user's reputation
                    reputation_system.log_report_submission(active_user, is_valid=False)
                    
                    # Warn the user
                    QtWidgets.QMessageBox.warning(
                        self,
                        "Rapid Submission Detected",
                        f"You've submitted reports too quickly (within {time_diff_seconds:.1f} seconds). "
                        "Please wait before submitting another report.\n\n"
                        "Continued rapid submissions may result in account restrictions."
                    )
                    return
            except Exception as e:
                print(f"Error checking submission time: {e}")
        
        # If in edit mode and we have report data and a parent screen
        if self.edit_mode and self.report_data and self.parent_screen:
            # We're updating an existing report
            # Create updated report data
            updated_report = {
                "location": address,
                "type": problem,
                "description": description,
                "image_path": self.report_data.get("image_path"),  # Keep existing image path
                "date": self.report_data.get("date"),  # Keep the original date
                "username": self.report_data.get("username", active_user),
                "status": self.report_data.get("status", "Submitted"),  # Keep existing status
                "coordinates": self.selected_coordinates  # Update coordinates if available
            }
            
            # Try to update via the parent screen's callback method
            try:
                parent_method = getattr(self.parent_screen, 'update_report_from_edit_screen')
                parent_method(self.report_id, updated_report)
                
                # Show success message for update
                QtWidgets.QMessageBox.information(
                    self,
                    "Report Updated",
                    f"Your report about '{problem}' at {address} has been updated successfully."
                )
                
                # Close this screen and return to parent
                self.close()
                if self.parent_screen:
                    self.parent_screen.show()
            except (AttributeError, TypeError) as e:
                print(f"Error calling update_report_from_edit_screen: {e}")
                print("Error: Parent screen does not have update_report_from_edit_screen method")
                QtWidgets.QMessageBox.critical(
                    self,
                    "Error",
                    "Could not update report. Please try again."
                )
        else:
            # Creating a new report
            # Check for duplicate reports
            if is_duplicate_report(address, problem):
                # Show duplicate warning message
                QtWidgets.QMessageBox.warning(
                    self,
                    "Duplicate Report",
                    f"A report for '{problem}' at '{address}' already exists.\n\nDuplicate reports are not allowed."
                )
                
                # Log this as potentially suspicious behavior
                reputation_system.log_report_submission(active_user, is_valid=False)
                return
                
            # Add to reports list if not a duplicate
            new_report = {
                "address": address,
                "problem": problem,
                "description": description,
                "image_path": None,  # We're not handling images yet
                "date": formatted_time,
                "username": active_user,
                "status": "Pending"
            }
            
            # Save to reports.json (main_ui handles this part)
            from main_ui import save_report
            save_report(new_report)
            
            # Log this report submission as valid and update last submission time
            reputation_system.log_report_submission(active_user, is_valid=True)
            
            # Show success message for new report
            QtWidgets.QMessageBox.information(
                self,
                "Report Submitted",
                f"Thank you for your report about '{problem}' at {address}. \n\n"
                "Your report has been submitted successfully and will be reviewed by our team."
            )
            
            # Go back to the main screen instead of just closing
            self.hide()
            from main_ui import MyMainScreen
            self.next = MyMainScreen()
            self.next.show()
    
    def cancel_clicked(self):
        """Return to the parent screen or main screen when cancel is clicked."""
        self.hide()
        
        if self.edit_mode and self.parent_screen:
            # Return to the parent screen (likely MyReportsScreen)
            self.parent_screen.show()
        else:
            # Go to main screen
            from main_ui import MyMainScreen
            self.next = MyMainScreen()
            self.next.show()
    
    def validate_inputs(self):
        """
        Validate that all required inputs are provided.
        
        Returns:
            bool: True if all inputs are valid, False otherwise
        """
        # Check if address is provided
        if not self.address_input.text().strip():
            QtWidgets.QMessageBox.warning(
                self,
                "Missing Information",
                "Please provide the address of the issue."
            )
            return False
        
        # Check if a problem type is selected
        if not self.get_selected_problem():
            QtWidgets.QMessageBox.warning(
                self,
                "Missing Information",
                "Please select the type of problem you are reporting."
            )
            return False
        
        return True
    
    def get_selected_problem(self):
        """
        Get the selected problem type.
        
        Returns:
            str: The name of the selected problem, or None if no problem is selected
        """
        for button in self.problems_group.buttons():
            if button.isChecked():
                return button.text()
        return None
    
    def open_map_dialog(self):
        """Open the map dialog to select a location."""
        map_dialog = MapDialog(self)
        map_dialog.addressSelected.connect(self.set_address)
        map_dialog.exec_()
    
    def set_address(self, address):
        """
        Set the address input with the selected address.
        
        Args:
            address (str): The address selected from the map
        """
        self.address_input.setText(address)


# For standalone testing
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # Apply stylesheet
    with open("modern_style.qss", "r") as f:
        app.setStyleSheet(f.read())
    
    report_screen = MyReportScreen()
    report_screen.show()
    sys.exit(app.exec_())
