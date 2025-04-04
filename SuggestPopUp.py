#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Suggest Popup Dialog Module

This module provides a dialog interface for suggesting solutions to reported problems.
It allows users to enter and submit solution suggestions for specific issues.
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SuggestPopUp(object):
    """
    UI class for the Suggest Popup Dialog.
    
    This class defines the user interface elements for the solution suggestion dialog,
    allowing users to enter and submit ideas for fixing reported problems.
    """
    
    def setupUi(self, SuggestPopUp):
        """
        Set up the user interface for the Suggest Popup Dialog.
        
        Args:
            SuggestPopUp (QDialog): The dialog to set up
        """
        SuggestPopUp.setObjectName("SuggestPopUp")
        SuggestPopUp.setWindowIcon(QtGui.QIcon('images/cypress_logo.png'))
        
        # Main layout
        self.verticalLayout = QtWidgets.QVBoxLayout(SuggestPopUp)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Header setup
        self._setup_header(SuggestPopUp)
        
        # Description setup
        self._setup_description(SuggestPopUp)
        
        # Content area setup
        self._setup_content_area(SuggestPopUp)
        
        # Buttons setup
        self._setup_buttons(SuggestPopUp)
        
        self.retranslateUi(SuggestPopUp)
        QtCore.QMetaObject.connectSlotsByName(SuggestPopUp)
    
    def _setup_header(self, SuggestPopUp):
        """Set up the header section of the dialog."""
        # Header label
        self.header_label = QtWidgets.QLabel(SuggestPopUp)
        font = QtGui.QFont()
        font.setFamily("Gubbi")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.header_label.setFont(font)
        self.header_label.setFrameShape(QtWidgets.QFrame.Box)
        self.header_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.header_label.setLineWidth(1)
        self.header_label.setMidLineWidth(0)
        self.header_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.header_label.setIndent(-1)
        self.header_label.setObjectName("header_label")
        self.verticalLayout.addWidget(self.header_label)
    
    def _setup_description(self, SuggestPopUp):
        """Set up the description section of the dialog."""
        # Description label
        self.description_label = QtWidgets.QLabel(SuggestPopUp)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.description_label.setFont(font)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.verticalLayout.addWidget(self.description_label)
    
    def _setup_content_area(self, SuggestPopUp):
        """Set up the content area of the dialog."""
        # Scroll area
        self.scrollArea = QtWidgets.QScrollArea(SuggestPopUp)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        
        # Scroll area contents
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 810, 261))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        # Layout for scroll area contents
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        # Frame for content
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        
        # Grid layout for frame
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        
        # Problem label
        self.problem_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.problem_label.setFont(font)
        self.problem_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.problem_label.setText("")
        self.problem_label.setWordWrap(True)
        self.problem_label.setObjectName("problem_label")
        self.gridLayout.addWidget(self.problem_label, 0, 0, 1, 2)
        
        # Solution input
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 1)
        
        # Solution label
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        
        # Add frame to vertical layout
        self.verticalLayout_2.addWidget(self.frame)
        
        # Set widget for scroll area
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
    
    def _setup_buttons(self, SuggestPopUp):
        """Set up the button section of the dialog."""
        # Create button font
        button_font = QtGui.QFont()
        button_font.setPointSize(11)
        
        # Back button
        self.back_button = QtWidgets.QPushButton(SuggestPopUp)
        self.back_button.setObjectName("back_button")
        self.back_button.setFont(button_font)
        self.back_button.setMinimumHeight(40)
        self.back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.back_button)
        
        # Submit button
        self.submit_button = QtWidgets.QPushButton(SuggestPopUp)
        self.submit_button.setObjectName("submit_button")
        self.submit_button.setFont(button_font)
        self.submit_button.setMinimumHeight(40)
        self.submit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.submit_button)
        
        # Cancel button
        self.cancel_button = QtWidgets.QPushButton(SuggestPopUp)
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setFont(button_font)
        self.cancel_button.setMinimumHeight(40)
        self.cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.cancel_button)
    
    def retranslateUi(self, SuggestPopUp):
        """
        Set the text for UI elements.
        
        Args:
            SuggestPopUp (QDialog): The dialog containing the UI elements
        """
        _translate = QtCore.QCoreApplication.translate
        SuggestPopUp.setWindowTitle(_translate("SuggestPopUp", "Suggest Solution"))
        self.header_label.setText(_translate("SuggestPopUp", "CYPRESS                                                                                  City of Toronto"))
        self.description_label.setText(_translate("SuggestPopUp", "Suggest a solution for this reported problem"))
        self.label.setText(_translate("SuggestPopUp", "Suggest solution:"))
        self.back_button.setText(_translate("SuggestPopUp", "Back"))
        self.submit_button.setText(_translate("SuggestPopUp", "Submit"))
        self.cancel_button.setText(_translate("SuggestPopUp", "Cancel"))


class SuggestPopUp(QtWidgets.QDialog, Ui_SuggestPopUp):
    """
    Functional implementation of the Suggest Popup Dialog.
    
    This class extends the UI definition with actual functionality, handling
    user interactions and connecting signals to slots.
    """
    
    def __init__(self, problem, parent=None):
        """
        Initialize the Suggest Popup Dialog with functionality.
        
        Args:
            problem (dict): Problem data to display and suggest a solution for
            parent (QWidget, optional): Parent widget. Defaults to None.
        """
        super(SuggestPopUp, self).__init__(parent)
        self.setupUi(self)
        
        # Store problem data
        self.problem = problem
        
        # Set dialog size and properties
        self.setMinimumSize(750, 600)
        self.setFixedSize(800, 650)
        self.setWindowTitle(f"Suggest Solution - {problem['problem_type']}")
        
        # Apply modern styling
        self.setStyleSheet("""
            QDialog {
                background-color: #f5f5f5;
            }
            QLabel {
                font-size: 14px;
            }
            QLabel[heading="true"] {
                font-size: 16px;
                font-weight: bold;
                color: #2c3e50;
            }
            QTextEdit {
                background-color: white;
                border-radius: 5px;
                border: 1px solid #ccc;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton {
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton#submitButton {
                background-color: #3498db;
                color: white;
            }
            QPushButton#cancelButton {
                background-color: #e74c3c;
                color: white;
            }
            QPushButton#likeButton, QPushButton#suggestButton {
                background-color: #3498db;
                color: white;
                padding: 10px 0px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton#cancelButton:hover {
                background-color: #c0392b;
            }
        """)
        
        # Display problem information
        self._display_problem_info()
        
        # Connect signals to slots
        self.connect_signals()
    
    def _display_problem_info(self):
        """Display the problem information in the dialog."""
        problem_text = (
            f"<b>{self.problem['problem_type']}</b><br>"
            f"At: {self.problem['address']}<br><br>"
            f"{self.problem['description']}"
        )
        self.problem_label.setText(problem_text)
    
    def connect_signals(self):
        """Connect button signals to their respective slots."""
        self.cancel_button.clicked.connect(self.reject)
        self.back_button.clicked.connect(self.reject)
        self.submit_button.clicked.connect(self.submit_solution)
    
    def submit_solution(self):
        """Submit the suggested solution."""
        solution_text = self.textEdit.toPlainText().strip()
        
        # Validate input
        if not solution_text:
            QtWidgets.QMessageBox.warning(
                self,
                "Empty Solution",
                "Please provide a solution suggestion before submitting."
            )
            return
        
        # Here you would typically save the solution to a database
        # For now, just show a success message
        QtWidgets.QMessageBox.information(
            self,
            "Solution Submitted",
            "Thank you for your suggestion! Your input will help improve the community."
        )
        
        self.accept()


# For standalone testing
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # Create sample problem data
    sample_problem = {
        "id": 1,
        "address": "123 Main St, Toronto",
        "problem_type": "Potholes",
        "description": "Large pothole causing traffic issues",
        "date_reported": "2023-03-15"
    }
    
    # Apply stylesheet if available
    try:
        with open("modern_style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except (FileNotFoundError, IOError):
        pass
    
    popup = SuggestPopUp(sample_problem)
    popup.exec_()
