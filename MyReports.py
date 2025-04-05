#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MyReports Module

This module provides the UI for the My Reports screen, where users can view
their submitted reports. It includes a scrollable area for displaying multiple
reports and buttons for editing and deleting reports.
"""

from PyQt5 import QtCore, QtGui, QtWidgets


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
        
        # Status button
        self.status_button = self._create_action_button("status_button", "Update Status")
        self.status_button.setStyleSheet("""
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
            QPushButton:disabled {
                background-color: #bdc3c7;
                color: #7f8c8d;
            }
        """)
        self.button_layout.addWidget(self.status_button)
        
        # Edit button
        self.edit_button = self._create_action_button("edit_button", "Edit")
        self.button_layout.addWidget(self.edit_button)
        
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


class MyReportsScreen(QtWidgets.QMainWindow):
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
        
        # Connect signals to slots
        self.ui.back_button.clicked.connect(self.back_clicked)
        self.ui.edit_button.clicked.connect(self.edit_report)
        self.ui.delete_button.clicked.connect(self.delete_report)
        self.ui.status_button.clicked.connect(self.update_status)
        
        # Populate with sample reports
        self.populate_reports()
    
    def populate_reports(self):
        """Populate the reports list with sample data."""
        sample_reports = [
            {"type": "Potholes", "location": "502 Jarvis Street, Toronto, Ontario"},
            {"type": "Utility Failures", "location": "Nelson Mandela Walk, Toronto, Ontario"},
            {"type": "Tree Collapse", "location": "123 Queen Street, Toronto, Ontario"},
            {"type": "Flooded Streets", "location": "456 King Street, Toronto, Ontario"}
        ]
        
        for i, report in enumerate(sample_reports):
            # Create a report item widget
            report_widget = QtWidgets.QWidget()
            report_widget.setObjectName(f"report_{i}")
            report_widget.setStyleSheet("""
                QWidget {
                    background-color: white;
                    border-radius: 8px;
                    border: 1px solid #ddd;
                }
                QWidget:hover {
                    border: 1px solid #3498db;
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
            type_label = QtWidgets.QLabel(report["type"])
            type_label.setMinimumWidth(200)
            type_label.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
            report_layout.addWidget(type_label)
            
            # Create label for report location
            location_label = QtWidgets.QLabel(report["location"])
            location_label.setFont(QtGui.QFont("Arial", 11))
            report_layout.addWidget(location_label)
            
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
        selected_button = self.ui.report_button_group.checkedButton()
        if not selected_button:
            QtWidgets.QMessageBox.warning(
                self,
                "No Selection",
                "Please select a report to edit."
            )
            return
        
        # Get the ID from the selected button
        report_id = self.ui.report_button_group.id(selected_button)
        QtWidgets.QMessageBox.information(
            self,
            "Edit Report",
            f"Editing report #{report_id + 1}"
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
        
        # Get the ID from the selected button
        report_id = self.ui.report_button_group.id(selected_button)
        reply = QtWidgets.QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete report #{report_id + 1}?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        
        if reply == QtWidgets.QMessageBox.Yes:
            # Remove the widget from the layout
            widget = self.ui.report_button_group.button(report_id).parent()
            self.ui.reports_layout.removeWidget(widget)
            widget.deleteLater()
            QtWidgets.QMessageBox.information(
                self,
                "Report Deleted",
                f"Report #{report_id + 1} has been deleted."
            )
    
    def update_status(self):
        """Update the status of the selected report."""
        selected_button = self.ui.report_button_group.checkedButton()
        if not selected_button:
            QtWidgets.QMessageBox.warning(
                self,
                "No Selection",
                "Please select a report to update its status."
            )
            return
        
        # Get the ID from the selected button
        report_id = self.ui.report_button_group.id(selected_button)
        QtWidgets.QMessageBox.information(
            self,
            "Update Status",
            f"Updating status of report #{report_id + 1}"
        )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    report_window = MyReportsScreen()
    report_window.show()
    sys.exit(app.exec_())
