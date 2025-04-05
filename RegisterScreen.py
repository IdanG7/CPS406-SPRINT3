#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
RegisterScreen Module

This module provides the UI for the user registration screen, allowing new users
to create accounts for the Cypress application. It includes form fields for personal
information and credentials, with validation for required fields.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from SQ_Dialog import Ui_SQ_Dialog


class Ui_RegisterScreen(object):
    """
    UI class for the Registration Screen.
    
    This class defines the user interface elements for the registration screen,
    allowing new users to create accounts with their personal information.
    """
    
    def setupUi(self, RegisterScreen):
        """
        Set up the user interface for the Registration Screen.
        
        Args:
            RegisterScreen (QMainWindow): The main window to set up
        """
        RegisterScreen.setObjectName("RegisterScreen")
        RegisterScreen.resize(900, 700)
        RegisterScreen.setWindowIcon(QtGui.QIcon("images/cypress_logo.png"))
        RegisterScreen.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
        """)
        
        # Create central widget and layout
        self.central_widget = QtWidgets.QWidget(RegisterScreen)
        self.central_widget.setObjectName("central_widget")
        self.main_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(30, 20, 30, 20)
        self.main_layout.setSpacing(20)
        self.main_layout.setObjectName("main_layout")
        
        # Create header section
        self.header_widget = QtWidgets.QWidget(self.central_widget)
        self.header_widget.setMaximumHeight(100)
        self.header_layout = QtWidgets.QHBoxLayout(self.header_widget)
        self.header_layout.setContentsMargins(10, 10, 10, 10)
        
        # Create CYPRESS header label
        self.header_label = QtWidgets.QLabel(self.header_widget)
        title_font = QtGui.QFont()
        title_font.setFamily("Arial")
        title_font.setPointSize(40)  # Increased font size further
        title_font.setBold(True)
        self.header_label.setFont(title_font)
        self.header_label.setStyleSheet("color: #2c3e50;")
        self.header_label.setAlignment(QtCore.Qt.AlignCenter)
        self.header_label.setObjectName("header_label")
        self.header_label.setText("City of Toronto - Cypress")  # Set text directly
        self.header_layout.addWidget(self.header_label, 1)  # Add stretch factor to center
        
        # Add header to main layout
        self.main_layout.addWidget(self.header_widget)
        
        # Add exit button in top right corner
        self.exit_button = QtWidgets.QPushButton(self.central_widget)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setMinimumSize(40, 40)
        self.exit_button.setMaximumSize(40, 40)
        self.exit_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 20px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #a93226;
            }
        """)
        self.exit_button.setText("X")
        self.exit_button.setToolTip("Exit Application")
        
        # Position the exit button in the top right corner
        self.exit_button.setGeometry(QtCore.QRect(RegisterScreen.width() - 50, 10, 40, 40))
        RegisterScreen.resizeEvent = lambda event: self.exit_button.setGeometry(
            QtCore.QRect(RegisterScreen.width() - 50, 10, 40, 40)
        )
        
        # Add separator line
        self.separator = QtWidgets.QFrame(self.central_widget)
        self.separator.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator.setStyleSheet("background-color: #bdc3c7;")
        self.main_layout.addWidget(self.separator)
        
        # Create description label
        self.description_label = QtWidgets.QLabel(self.central_widget)
        description_font = QtGui.QFont()
        description_font.setPointSize(14)
        description_font.setBold(False)
        self.description_label.setFont(description_font)
        self.description_label.setWordWrap(True)
        self.description_label.setAlignment(QtCore.Qt.AlignCenter)
        self.description_label.setStyleSheet("color: #34495e; margin: 10px 0;")
        self.description_label.setObjectName("description_label")
        self.description_label.setText("Please enter your information below:")
        self.main_layout.addWidget(self.description_label)
        
        # Create form container
        self.form_container = QtWidgets.QWidget(self.central_widget)
        self.form_container.setObjectName("form_container")
        self.form_container.setStyleSheet("""
            QWidget#form_container {
                background-color: white;
                border-radius: 8px;
                border: 1px solid #e0e0e0;
            }
        """)
        
        # Create form layout
        self.form_layout = QtWidgets.QFormLayout(self.form_container)
        self.form_layout.setContentsMargins(40, 30, 40, 30)
        self.form_layout.setSpacing(15)
        self.form_layout.setLabelAlignment(QtCore.Qt.AlignRight)
        self.form_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        
        # Create form field style
        input_style = """
            QLineEdit {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 8px;
                background-color: white;
                color: #2c3e50;
                font-size: 14px;
                min-height: 30px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
        """
        
        # Create label style
        label_style = "color: #2c3e50; font-size: 14px; font-weight: bold;"
        
        # First Name field
        self.fn_label = QtWidgets.QLabel(self.form_container)
        self.fn_label.setObjectName("fn_label")
        self.fn_label.setStyleSheet(label_style)
        self.fn_label.setText("First Name:")
        self.first_name = QtWidgets.QLineEdit(self.form_container)
        self.first_name.setObjectName("first_name")
        self.first_name.setStyleSheet(input_style)
        self.form_layout.addRow(self.fn_label, self.first_name)
        
        # Last Name field
        self.ln_label = QtWidgets.QLabel(self.form_container)
        self.ln_label.setObjectName("ln_label")
        self.ln_label.setStyleSheet(label_style)
        self.ln_label.setText("Last Name:")
        self.last_name = QtWidgets.QLineEdit(self.form_container)
        self.last_name.setObjectName("last_name")
        self.last_name.setStyleSheet(input_style)
        self.form_layout.addRow(self.ln_label, self.last_name)
        
        # Address field
        self.address_label = QtWidgets.QLabel(self.form_container)
        self.address_label.setObjectName("address_label")
        self.address_label.setStyleSheet(label_style)
        self.address_label.setText("Address:")
        self.address = QtWidgets.QLineEdit(self.form_container)
        self.address.setObjectName("address")
        self.address.setStyleSheet(input_style)
        self.form_layout.addRow(self.address_label, self.address)
        
        # Phone Number field
        self.phone_label = QtWidgets.QLabel(self.form_container)
        self.phone_label.setObjectName("phone_label")
        self.phone_label.setStyleSheet(label_style)
        self.phone_label.setText("Phone Number:")
        
        # Create phone number container with 3 fields and dashes
        self.phone_container = QtWidgets.QWidget(self.form_container)
        self.phone_layout = QtWidgets.QHBoxLayout(self.phone_container)
        self.phone_layout.setContentsMargins(0, 0, 0, 0)
        self.phone_layout.setSpacing(5)
        
        self.phone_1 = QtWidgets.QLineEdit(self.phone_container)
        self.phone_1.setMaximumWidth(60)
        self.phone_1.setObjectName("phone_1")
        self.phone_1.setStyleSheet(input_style)
        self.phone_layout.addWidget(self.phone_1)
        
        self.dash_label1 = QtWidgets.QLabel(self.phone_container)
        self.dash_label1.setText("-")
        self.dash_label1.setStyleSheet("color: #2c3e50; font-size: 16px;")
        self.phone_layout.addWidget(self.dash_label1)
        
        self.phone_2 = QtWidgets.QLineEdit(self.phone_container)
        self.phone_2.setMaximumWidth(60)
        self.phone_2.setObjectName("phone_2")
        self.phone_2.setStyleSheet(input_style)
        self.phone_layout.addWidget(self.phone_2)
        
        self.dash_label2 = QtWidgets.QLabel(self.phone_container)
        self.dash_label2.setText("-")
        self.dash_label2.setStyleSheet("color: #2c3e50; font-size: 16px;")
        self.phone_layout.addWidget(self.dash_label2)
        
        self.phone_3 = QtWidgets.QLineEdit(self.phone_container)
        self.phone_3.setMaximumWidth(80)
        self.phone_3.setObjectName("phone_3")
        self.phone_3.setStyleSheet(input_style)
        self.phone_layout.addWidget(self.phone_3)
        
        # Add spacer to push phone fields to the left
        self.phone_layout.addStretch()
        
        self.form_layout.addRow(self.phone_label, self.phone_container)
        
        # Email field
        self.email_label = QtWidgets.QLabel(self.form_container)
        self.email_label.setObjectName("email_label")
        self.email_label.setStyleSheet(label_style)
        self.email_label.setText("Email Address:")
        
        # Create email container with field and domain
        self.email_container = QtWidgets.QWidget(self.form_container)
        self.email_layout = QtWidgets.QHBoxLayout(self.email_container)
        self.email_layout.setContentsMargins(0, 0, 0, 0)
        self.email_layout.setSpacing(0)
        
        self.email_address = QtWidgets.QLineEdit(self.email_container)
        self.email_address.setObjectName("email_address")
        self.email_address.setStyleSheet(input_style)
        self.email_layout.addWidget(self.email_address)
        
        self.email_domain_label = QtWidgets.QLabel(self.email_container)
        self.email_domain_label.setObjectName("email_domain_label")
        self.email_domain_label.setStyleSheet("color: #2c3e50; font-size: 14px; font-weight: bold; padding-left: 5px;")
        self.email_domain_label.setText("@cypress.on.ca")
        self.email_layout.addWidget(self.email_domain_label)
        
        # Add spacer to push email fields to the left
        self.email_layout.addStretch()
        
        self.form_layout.addRow(self.email_label, self.email_container)
        
        # Username field
        self.username_label = QtWidgets.QLabel(self.form_container)
        self.username_label.setObjectName("username_label")
        self.username_label.setStyleSheet(label_style)
        self.username_label.setText("Username:")
        self.username = QtWidgets.QLineEdit(self.form_container)
        self.username.setObjectName("username")
        self.username.setStyleSheet(input_style)
        self.form_layout.addRow(self.username_label, self.username)
        
        # Password field
        self.password_label = QtWidgets.QLabel(self.form_container)
        self.password_label.setObjectName("password_label")
        self.password_label.setStyleSheet(label_style)
        self.password_label.setText("Password:")
        self.password = QtWidgets.QLineEdit(self.form_container)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.password.setStyleSheet(input_style)
        self.form_layout.addRow(self.password_label, self.password)
        
        # Password requirements hint
        self.password_hint = QtWidgets.QLabel(self.form_container)
        self.password_hint.setObjectName("password_hint")
        self.password_hint.setStyleSheet("color: #7f8c8d; font-size: 12px; font-style: italic;")
        self.password_hint.setText("Password must be at least 8 characters and include uppercase, lowercase, and numbers")
        self.password_hint.setWordWrap(True)
        self.form_layout.addRow("", self.password_hint)
        
        # Add spacer before buttons
        self.form_layout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        
        # Create buttons container
        self.button_container = QtWidgets.QWidget(self.form_container)
        self.button_layout = QtWidgets.QHBoxLayout(self.button_container)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setSpacing(20)
        
        # Create register button
        self.register_button = QtWidgets.QPushButton(self.button_container)
        self.register_button.setMinimumSize(QtCore.QSize(200, 50))
        self.register_button.setObjectName("register_button")
        self.register_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
            QPushButton:pressed {
                background-color: #219653;
            }
        """)
        self.register_button.setText("Register")
        self.button_layout.addWidget(self.register_button)
        
        # Create cancel button
        self.cancel_button = QtWidgets.QPushButton(self.button_container)
        self.cancel_button.setMinimumSize(QtCore.QSize(200, 50))
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 5px;
                padding: 10px;
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
        self.cancel_button.setText("Cancel")
        self.button_layout.addWidget(self.cancel_button)
        
        # Add buttons to form layout
        self.form_layout.addRow("", self.button_container)
        
        # Add form container to main layout
        self.main_layout.addWidget(self.form_container)
        
        # Set central widget
        RegisterScreen.setCentralWidget(self.central_widget)
        
        # Create menubar and statusbar
        self.menu_bar = QtWidgets.QMenuBar(RegisterScreen)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menu_bar.setObjectName("menu_bar")
        RegisterScreen.setMenuBar(self.menu_bar)
        
        self.status_bar = QtWidgets.QStatusBar(RegisterScreen)
        self.status_bar.setObjectName("status_bar")
        RegisterScreen.setStatusBar(self.status_bar)
        
        # Set text for all UI elements directly
        RegisterScreen.setWindowTitle("Cypress")


class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SQ_Dialog()
        self.ui.setupUi(self)
        
        # Connect exit button
        self.ui.exit_button.clicked.connect(self.exit_clicked)
        
        # Create and configure the security question text field
        self.ui.security_question = QtWidgets.QLineEdit(self)
        self.ui.security_question.setGeometry(QtCore.QRect(190, 170, 381, 51))
        self.ui.security_question.setObjectName("security_question")
        self.ui.security_question.setStyleSheet("""
            QLineEdit {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 8px;
                background-color: white;
                color: #2c3e50;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
        """)
        
        # Style the description label
        self.ui.description_label.setStyleSheet("color: #2980b9; font-weight: bold;")
        
        # Set the state for tracking dialog result
        self.state = ""

        # Set text directly
        self.ui.description_label.setText(
            "Your registration is almost complete! Enter a security question and answer to verify your identity should you forget your password"
        )
            
        # Connect OK button to close method
        self.ui.OK_Button.clicked.connect(self.close)

    def close(self):
        """Hide the dialog when closed and set state to OK."""
        self.state = "OK"
        self.hide()

    def exit_clicked(self):
        """Exit the application after confirmation."""
        from PyQt5.QtWidgets import QMessageBox, QApplication
        reply = QMessageBox.question(
            self, 
            'Exit Confirmation',
            'Are you sure you want to exit the application?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            QApplication.quit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    RegisterScreen = QtWidgets.QMainWindow()
    ui = Ui_RegisterScreen()
    ui.setupUi(RegisterScreen)
    RegisterScreen.showFullScreen()
    sys.exit(app.exec_())
