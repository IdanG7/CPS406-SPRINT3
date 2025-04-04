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
        
        # Add the widget to the scroll area
        self.report_scroll_area.setWidget(self.scroll_content_widget)
        self.main_layout.addWidget(self.report_scroll_area, 1, 0, 1, 3)
        
        # Create buttons for actions
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        self.button_layout.setSpacing(10)  # Add spacing between buttons
        
        # Back button
        self.back_button = self._create_action_button("back_button", "Back")
        self.button_layout.addWidget(self.back_button)
        
        # Edit button
        self.edit_button = self._create_action_button("edit_button", "Edit")
        self.button_layout.addWidget(self.edit_button)
        
        # Delete button
        self.delete_button = self._create_action_button("delete_button", "Delete")
        self.button_layout.addWidget(self.delete_button)
        
        # Add buttons to the main layout
        self.main_layout.addLayout(self.button_layout, 2, 0, 1, 3)
        
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    report_window = QtWidgets.QMainWindow()
    ui = Ui_MyReports()
    ui.setupUi(report_window)
    report_window.show()
    sys.exit(app.exec_())
