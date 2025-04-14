#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MyReports Module

This module provides the UI for the My Reports screen, where users can view
their submitted reports. It includes a scrollable area for displaying multiple
reports and buttons for editing and deleting reports.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
import json
import os

# Define path for the reports JSON file
REPORTS_FILE = 'reports.json'

class Ui_MyReports(object):
    """
    UI class for the My Reports screen.
    
    This class defines the user interface elements for the My Reports screen,
    allowing users to view, edit, and delete their submitted reports.
    """
    
    def setupUi(self, report_window):
        """
        Set up the user interface for the My Reports screen.
        
        Args:
            report_window (QMainWindow): The main window to set up
        """
        report_window.setObjectName("MyReports")
        # Set a larger fixed size to accommodate more content
        report_window.setFixedSize(1500, 700)
        
        # Create central widget and layout
        self.central_widget = QtWidgets.QWidget(report_window)
        self.central_widget.setObjectName("central_widget")
        self.main_layout = QtWidgets.QGridLayout(self.central_widget)
        self.main_layout.setObjectName("main_layout")
        
        # Create header label
        self.header_label = QtWidgets.QLabel(self.central_widget)
        header_font = QtGui.QFont()
        header_font.setFamily("Arial")
        header_font.setPointSize(20)
        header_font.setBold(True)
        header_font.setWeight(75)
        self.header_label.setFont(header_font)
        self.header_label.setAlignment(QtCore.Qt.AlignCenter)
        self.header_label.setObjectName("header_label")
        self.main_layout.addWidget(self.header_label, 0, 0, 1, 3)
        
        # Create scrollable area for reports with increased size
        self.report_scroll_area = QtWidgets.QScrollArea(self.central_widget)
        self.report_scroll_area.setWidgetResizable(True)
        self.report_scroll_area.setMinimumHeight(500)  # Ensure enough height for reports
        self.report_scroll_area.setObjectName("report_scroll_area")
        
        # Apply styling to the scroll area for better visibility
        self.report_scroll_area.setStyleSheet("""
            QScrollArea {
                border: 1px solid #ccc;
                background-color: #f9f9f9;
            }
            QScrollBar:vertical {
                width: 12px;
                background: #f0f0f0;
            }
            QScrollBar::handle:vertical {
                background: #888;
                border-radius: 6px;
            }
        """)
        
        # Create widget to hold the reports
        self.scroll_content_widget = QtWidgets.QWidget()
        self.scroll_content_widget.setGeometry(QtCore.QRect(0, 0, 1480, 480))
        self.scroll_content_widget.setObjectName("scroll_content_widget")
        
        # Create vertical layout for reports
        self.reports_layout = QtWidgets.QVBoxLayout(self.scroll_content_widget)
        self.reports_layout.setObjectName("reports_layout")
        self.reports_layout.setSpacing(15)  # Add spacing between reports
        self.reports_layout.setContentsMargins(10, 10, 10, 10)  # Add padding
        
        # Create a button group to ensure only one report can be selected at a time
        self.report_button_group = QtWidgets.QButtonGroup(self.central_widget)
        self.report_button_group.setExclusive(True)  # Only one can be selected
        
        # Add the widget to the scroll area
        self.report_scroll_area.setWidget(self.scroll_content_widget)
        self.main_layout.addWidget(self.report_scroll_area, 1, 0, 1, 3)
        
        # Create buttons for actions
        self._setup_buttons()
        
        # Set the central widget
        report_window.setCentralWidget(self.central_widget)
        
        # Create menu and status bars
        self.menu_bar = QtWidgets.QMenuBar(report_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1500, 22))
        self.menu_bar.setObjectName("menu_bar")
        report_window.setMenuBar(self.menu_bar)
        
        self.status_bar = QtWidgets.QStatusBar(report_window)
        self.status_bar.setObjectName("status_bar")
        report_window.setStatusBar(self.status_bar)
        
        # Set text for all UI elements
        self.set_ui_text(report_window)
        QtCore.QMetaObject.connectSlotsByName(report_window)
    
    def _setup_buttons(self):
        """Set up the action buttons."""
        # Create button layout
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        self.button_layout.setSpacing(10)  # Add spacing between buttons
        
        # Back button
        self.back_button = self._create_action_button("back_button", "Back")
        self.button_layout.addWidget(self.back_button)
        
        # Add spacer to push buttons to the right
        spacer = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.button_layout.addItem(spacer)
        
        # Delete button
        self.delete_button = self._create_action_button("delete_button", "Delete")
        self.delete_button.setStyleSheet("""
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
            QPushButton:disabled {
                background-color: #bdc3c7;
                color: #7f8c8d;
            }
        """)
        self.button_layout.addWidget(self.delete_button)
        
        # Add button layout to main layout
        self.main_layout.addLayout(self.button_layout, 2, 0, 1, 3)
    
    def _create_action_button(self, object_name, text):
        """
        Create a styled action button.
        
        Args:
            object_name (str): Object name for the button
            text (str): Text to display on the button
            
        Returns:
            QPushButton: The styled button
        """
        button = QtWidgets.QPushButton(self.central_widget)
        button.setMinimumSize(QtCore.QSize(0, 40))
        button.setObjectName(object_name)
        button.setText(text)
        button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f6dad;
            }
        """)
        return button
    
    def set_ui_text(self, report_window):
        """
        Set the text for all UI elements.
        
        Args:
            report_window (QMainWindow): The main window containing the UI elements
        """
        report_window.setWindowTitle("My Reports")
        self.header_label.setText("MY REPORTS")
        # Button texts are set in _create_action_button


class MyReportsScreen(QMainWindow):
    """
    Functional implementation of the My Reports Screen.
    
    This class extends the UI definition with actual functionality, handling
    user interactions and connecting signals to slots.
    """
    
    def __init__(self, parent=None):
        """
        Initialize the My Reports Screen with functionality.
        
        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
        """
        super(MyReportsScreen, self).__init__(parent)
        self.ui = Ui_MyReports()
        self.ui.setupUi(self)
        
        # Connect buttons to their functions
        self.ui.back_button.clicked.connect(self.back_clicked)
        self.ui.edit_button.clicked.connect(self.edit_report)
        self.ui.delete_button.clicked.connect(self.delete_report)
        
        # Load reports data from JSON
        self.reports = [] # Initialize as empty list
        self._load_reports()
        
        # Populate the reports list
        self.populate_reports()

    def _load_reports(self):
        """Load reports from the JSON file."""
        if os.path.exists(REPORTS_FILE):
            try:
                with open(REPORTS_FILE, 'r') as f:
                    self.reports = json.load(f)
                    # Ensure it's a list
                    if not isinstance(self.reports, list):
                        print(f"Warning: {REPORTS_FILE} does not contain a list. Initializing empty.")
                        self.reports = []
            except json.JSONDecodeError:
                print(f"Error: Could not decode JSON from {REPORTS_FILE}. Initializing empty.")
                self.reports = []
            except Exception as e:
                print(f"Error loading reports: {e}")
                self.reports = []
        else:
            print(f"Info: {REPORTS_FILE} not found. Initializing empty list.")
            self.reports = []

    def _save_reports(self):
        """Save the current reports list to the JSON file."""
        try:
            with open(REPORTS_FILE, 'w') as f:
                json.dump(self.reports, f, indent=4)
        except IOError as e:
            print(f"Error saving reports to {REPORTS_FILE}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while saving reports: {e}")

    def populate_reports(self):
        """Populate the reports list from self.reports data."""
        # Clear any existing reports
        for i in reversed(range(self.ui.reports_layout.count())):
            widget = self.ui.reports_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        
        # Add each report to the layout
        for i, report in enumerate(self.reports):
            # Create a widget for the report
            report_widget = QtWidgets.QWidget()
            report_widget.setObjectName(f"report_{i}")
            report_widget.setProperty("report_id", i)
            report_widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            
            # Double-click event for showing on map
            report_widget.mouseDoubleClickEvent = lambda event, idx=i: self.show_report_on_map(idx)
            
            # Style the widget
            report_widget.setStyleSheet("""
                QWidget {
                    background-color: #f8f8f8;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    padding: 10px;
                }
                QWidget:hover {
                    background-color: #f0f0f0;
                    border: 1px solid #ccc;
                }
            """)
            
            # Create layout for the report item
            report_layout = QtWidgets.QHBoxLayout(report_widget)
            report_layout.setContentsMargins(10, 10, 10, 10)
            
            # Create radio button for selection
            radio_button = QtWidgets.QRadioButton()
            radio_button.setObjectName(f"radio_{i}")
            radio_button.setMinimumSize(20, 20)
            report_layout.addWidget(radio_button)
            
            # Add to button group
            self.ui.report_button_group.addButton(radio_button, i)
            
            # Create label for report type
            # Use .get() for safer access in case keys are missing
            type_label = QtWidgets.QLabel(report.get("type", "N/A"))
            type_label.setMinimumWidth(200)
            type_label.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
            report_layout.addWidget(type_label)
            
            # Create label for report location
            location_label = QtWidgets.QLabel(report.get("location", "N/A"))
            location_label.setFont(QtGui.QFont("Arial", 11))
            report_layout.addWidget(location_label)
            
            # Create label for report status
            status_label = QtWidgets.QLabel(report.get("status", "N/A"))
            status_label.setFont(QtGui.QFont("Arial", 11))
            status_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            status_label.setMinimumWidth(100)
            
            # Style the status label based on status
            status = report.get("status", "N/A")
            if status == "Submitted":
                status_label.setStyleSheet("color: #ff9800;")  # Orange
            elif status == "In Progress":
                status_label.setStyleSheet("color: #2196f3;")  # Blue
            elif status == "Completed":
                status_label.setStyleSheet("color: #4caf50;")  # Green
            
            report_layout.addWidget(status_label)
            
            # Add to reports layout
            self.ui.reports_layout.addWidget(report_widget)
    
    def back_clicked(self):
        """Return to the main screen."""
        self.hide()
        from main_ui import MyMainScreen
        self.next = MyMainScreen()
        self.next.show()
    
    def edit_report(self):
        """Edit the selected report."""
        print("\n--- Starting edit_report ---")
        selected_button = self.ui.report_button_group.checkedButton()
        if not selected_button:
            QtWidgets.QMessageBox.warning(
                self,
                "No Selection",
                "Please select a report to edit."
            )
            return
        
        # Get the ID (index) from the selected button
        report_id = self.ui.report_button_group.id(selected_button)
        print(f"Selected report ID: {report_id}")

        # Check if report_id is valid
        if report_id < 0 or report_id >= len(self.reports):
            print(f"Error: Invalid report index {report_id}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Invalid report selection (index {report_id}).")
            return

        # Get the report data
        report = self.reports[report_id]
        print(f"Report data: {report}")
        
        # Hide THIS window
        self.hide()
        
        # Open the ReportScreen in EDIT MODE with existing report data
        from ReportScreen import MyReportScreen
        # Pass edit_mode=True, report_data, and report_id to enable edit mode
        self.edit_screen = MyReportScreen(
            parent=self,             # Set this as parent for callbacks
            edit_mode=True,          # Enable edit mode
            report_data=report,      # Pass report data to populate form
            report_id=report_id      # Pass report ID for update handling
        )
        self.edit_screen.show()
    
    def update_report_from_edit_screen(self, report_id, updated_report):
        """
        Receive and process updates from the Edit Report Screen.
        
        Args:
            report_id (int): The ID of the report to update
            updated_report (dict): The updated report data
        """
        # Update the report in our list
        if 0 <= report_id < len(self.reports):
            # Update only the fields that should change
            self.reports[report_id]["location"] = updated_report["location"]
            self.reports[report_id]["type"] = updated_report["type"]
            self.reports[report_id]["description"] = updated_report["description"]
            
            print(f"Updated report {report_id}: {self.reports[report_id]}")
            
            # Save changes to JSON file
            self._save_reports()
            
            # Refresh the reports list
            self.populate_reports()
        else:
            print(f"Error: Invalid report ID {report_id} for update")
            QtWidgets.QMessageBox.critical(
                self,
                "Error",
                f"Could not update report. Invalid report ID: {report_id}"
            )

    def delete_report(self):
        """Delete the selected report."""
        selected_button = self.ui.report_button_group.checkedButton()
        if not selected_button:
            QtWidgets.QMessageBox.warning(
                self,
                "No Selection",
                "Please select a report to delete."
            )
            return
        
        # Get the ID (index) from the selected button
        report_id = self.ui.report_button_group.id(selected_button)

        # Check if report_id is valid
        if report_id < 0 or report_id >= len(self.reports):
            print(f"Error: Invalid report index {report_id} for deletion.")
            QtWidgets.QMessageBox.critical(self, "Error", f"Invalid report selection for deletion (index {report_id}).")
            return

        reply = QtWidgets.QMessageBox.question(
            self, 
            'Confirm Delete',
            f"Are you sure you want to delete the report for '{self.reports[report_id].get('location', 'N/A')}'?", 
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, 
            QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            # Remove the report from the list
            del self.reports[report_id]
            
            # Save the updated list back to JSON
            self._save_reports()
            
            # Repopulate the list display
            self.populate_reports()
            
            QtWidgets.QMessageBox.information(
                self, 
                "Report Deleted", 
                "The selected report has been deleted."
            )

    def show_report_on_map(self, report_index):
        """Show the selected report's location on the map dialog."""
        if 0 <= report_index < len(self.reports):
            report = self.reports[report_index]
            location = report.get('location')
            coordinates = report.get('coordinates') # Get coordinates if available

            if location:
                # Import locally
                from MapDialog import MapDialog 
                
                # Pass coordinates if available, otherwise just the address
                map_dialog = MapDialog(parent=self)
                if coordinates and isinstance(coordinates, dict) and 'lat' in coordinates and 'lng' in coordinates:
                     map_dialog.display_location(location, coordinates['lat'], coordinates['lng'])
                else:
                     map_dialog.display_address(location)
                map_dialog.exec_() # Show as modal dialog
            else:
                QtWidgets.QMessageBox.warning(self, "No Location", "This report does not have a location specified.")
        else:
            print(f"Error: Invalid report index {report_index} for map display.")
