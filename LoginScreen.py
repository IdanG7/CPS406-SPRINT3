#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
LoginScreen Module

This module provides the login interface for the Cypress application.
It contains the UI definition for the login screen that users see
when accessing the system, with options for logging in, registering,
and recovering forgotten passwords.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from SQ_Dialog import Ui_SQ_Dialog


class Ui_LoginScreen(object):
    """
    UI class for the Login Screen.
    
    This class defines the user interface elements for the login screen,
    allowing users to authenticate to access the application.
    """
    
    def setupUi(self, login_window):
        """
        Set up the user interface for the Login Screen.
        
        Args:
            login_window (QMainWindow): The main window to set up
        """
        login_window.setObjectName("LoginScreen")
        login_window.resize(900, 600)
        login_window.setWindowIcon(QtGui.QIcon('images/cypress_logo.png'))
        login_window.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
        """)
        
        # Create central widget and layout
        self.central_widget = QtWidgets.QWidget(login_window)
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
        self.app_title_label = QtWidgets.QLabel(self.header_widget)
        title_font = QtGui.QFont()
        title_font.setFamily("Arial")
        title_font.setPointSize(36)  # Increased font size further
        title_font.setBold(True)
        self.app_title_label.setFont(title_font)
        self.app_title_label.setStyleSheet("color: #2c3e50;")
        self.app_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.app_title_label.setObjectName("app_title_label")
        self.header_layout.addWidget(self.app_title_label)
        
        # Create City of Toronto header label
        self.city_label = QtWidgets.QLabel(self.header_widget)
        self.city_label.setFont(title_font)
        self.city_label.setStyleSheet("color: #2c3e50;")
        self.city_label.setAlignment(QtCore.Qt.AlignCenter)
        self.city_label.setObjectName("city_label")
        self.header_layout.addWidget(self.city_label)
        
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
        self.exit_button.setGeometry(QtCore.QRect(login_window.width() - 50, 10, 40, 40))
        login_window.resizeEvent = lambda event: self.exit_button.setGeometry(
            QtCore.QRect(login_window.width() - 50, 10, 40, 40)
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
        self.description_label.setStyleSheet("color: #34495e; margin: 20px 0;")
        self.description_label.setObjectName("description_label")
        self.main_layout.addWidget(self.description_label)
        
        # Create login form container
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
        self.form_layout = QtWidgets.QVBoxLayout(self.form_container)
        self.form_layout.setContentsMargins(40, 30, 40, 30)
        self.form_layout.setSpacing(15)
        
        # Create username section
        self.username_container = QtWidgets.QWidget()
        self.username_layout = QtWidgets.QHBoxLayout(self.username_container)
        self.username_layout.setContentsMargins(0, 0, 0, 0)
        
        self.username_label = QtWidgets.QLabel()
        username_font = QtGui.QFont()
        username_font.setPointSize(12)
        username_font.setBold(True)
        self.username_label.setFont(username_font)
        self.username_label.setMinimumWidth(120)
        self.username_label.setStyleSheet("color: #2c3e50;")
        self.username_label.setObjectName("username_label")
        self.username_layout.addWidget(self.username_label)
        
        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setMinimumSize(QtCore.QSize(250, 40))
        self.username_input.setObjectName("username_input")
        self.username_input.setStyleSheet("""
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
        self.username_layout.addWidget(self.username_input)
        
        self.email_domain_label = QtWidgets.QLabel()
        self.email_domain_label.setFont(username_font)
        self.email_domain_label.setStyleSheet("color: #2c3e50;")
        self.email_domain_label.setObjectName("email_domain_label")
        self.username_layout.addWidget(self.email_domain_label)
        
        self.form_layout.addWidget(self.username_container)
        
        # Create password section
        self.password_container = QtWidgets.QWidget()
        self.password_layout = QtWidgets.QHBoxLayout(self.password_container)
        self.password_layout.setContentsMargins(0, 0, 0, 0)
        
        self.password_label = QtWidgets.QLabel()
        self.password_label.setFont(username_font)
        self.password_label.setMinimumWidth(120)
        self.password_label.setStyleSheet("color: #2c3e50;")
        self.password_label.setObjectName("password_label")
        self.password_layout.addWidget(self.password_label)
        
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setMinimumSize(QtCore.QSize(250, 40))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.password_input.setStyleSheet("""
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
        self.password_layout.addWidget(self.password_input)
        
        # Add spacer to align with username field
        spacer = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.password_layout.addItem(spacer)
        
        self.form_layout.addWidget(self.password_container)
        
        # Create forgot password button
        self.forgot_button = QtWidgets.QPushButton()
        self.forgot_button.setObjectName("forgot_button")
        self.forgot_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #3498db;
                text-decoration: underline;
                border: none;
                text-align: right;
                padding: 5px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                color: #2980b9;
            }
        """)
        self.form_layout.addWidget(self.forgot_button, 0, QtCore.Qt.AlignRight)
        
        # Create register button
        self.register_button = QtWidgets.QPushButton()
        self.register_button.setObjectName("register_button")
        self.register_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #3498db;
                text-decoration: underline;
                border: none;
                text-align: center;
                padding: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                color: #2980b9;
            }
        """)
        self.form_layout.addWidget(self.register_button, 0, QtCore.Qt.AlignCenter)
        
        # Add spacer before buttons
        self.form_layout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        
        # Create buttons container
        self.button_container = QtWidgets.QWidget()
        self.button_layout = QtWidgets.QHBoxLayout(self.button_container)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setSpacing(20)
        
        # Create login button
        self.login_button = QtWidgets.QPushButton()
        self.login_button.setMinimumSize(QtCore.QSize(200, 50))
        self.login_button.setObjectName("login_button")
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 5px;
                padding: 10px;
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
        self.button_layout.addWidget(self.login_button)
        
        # Create cancel button
        self.cancel_button = QtWidgets.QPushButton()
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
        self.button_layout.addWidget(self.cancel_button)
        
        self.form_layout.addWidget(self.button_container, 0, QtCore.Qt.AlignCenter)
        
        # Add form container to main layout
        self.main_layout.addWidget(self.form_container)
        
        # Set central widget
        login_window.setCentralWidget(self.central_widget)
        
        # Create menubar and statusbar
        self.menu_bar = QtWidgets.QMenuBar(login_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menu_bar.setObjectName("menu_bar")
        login_window.setMenuBar(self.menu_bar)
        
        self.status_bar = QtWidgets.QStatusBar(login_window)
        self.status_bar.setObjectName("status_bar")
        login_window.setStatusBar(self.status_bar)
        
        # Set text for all UI elements
        self.set_ui_text(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)
    
    def set_ui_text(self, login_window):
        """
        Set the text for all UI elements.
        
        Args:
            login_window (QMainWindow): The main window containing the UI elements
        """
        login_window.setWindowTitle("Cypress")
        self.app_title_label.setText("City of Toronto - Cypress")
        self.city_label.setText("")
        self.description_label.setText("You are currently at the Cypress Login Page. By logging into this system, you will be able to report a variety of problems as you have witnessed on the streets of Toronto.")
        self.username_label.setText("Username:")
        self.password_label.setText("Password:")
        self.email_domain_label.setText("@cypress.on.ca")
        self.forgot_button.setText("FORGOT PASSWORD?")
        self.register_button.setText("Don't have an account? REGISTER")
        self.login_button.setText("LOGIN")
        self.cancel_button.setText("BACK")
        self.exit_button.setText("X")


class SecurityQuestionDialog(QtWidgets.QDialog):
    """
    Dialog for security question verification.
    
    This dialog is shown when a user forgets their password and needs
    to verify their identity through a security question.
    """
    
    def __init__(self, answer):
        """
        Initialize the security question dialog.
        
        Args:
            answer (str): The security question answer
        """
        super().__init__()
        self.ui = Ui_SQ_Dialog()
        self.ui.setupUi(self)
        
        # Style the description label
        self.ui.description_label.setStyleSheet("color:rgb(32, 74, 135)")
        
        # Create and configure the security question text browser
        self.ui.security_question = QtWidgets.QTextBrowser(self)
        self.ui.security_question.setGeometry(QtCore.QRect(190, 170, 360, 101))
        self.ui.security_question.setObjectName("security_question")
        self.ui.security_question.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.ui.security_question.setAlignment(QtCore.Qt.AlignTop)
        self.ui.security_question.setText(answer)
        
        # Set font for security question
        question_font = QtGui.QFont()
        question_font.setFamily("Noto Mono")
        question_font.setPointSize(13)
        self.ui.security_question.setFont(question_font)
        
        # Set text
        self.set_english_text(self.ui)
        
        # Connect OK button to close method
        self.ui.OK_Button.clicked.connect(self.close)
    
    def close(self):
        """Hide the dialog when closed."""
        self.hide()
    
    def set_english_text(self, ui):
        """
        Set English text for the dialog.
        
        Args:
            ui (Ui_SQ_Dialog): The UI object to update
        """
        ui.retranslateUi(self)
        ui.description_label.setText("Enter your security question and answer below. After verification, your password will be sent to your account.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()
    ui = Ui_LoginScreen()
    ui.setupUi(login_window)
    ui.showFullScreen()  # Open in maximized window instead of normal size
    sys.exit(app.exec_())
