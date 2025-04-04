#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MainScreen Module

This module provides the main screen interface for the Cypress application.
It contains the UI definition for the main navigation screen that users see
after logging in, with options for reporting problems, viewing reports, etc.
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainScreen(object):
    """
    UI class for the Main Screen.
    
    This class defines the user interface elements for the main navigation screen,
    allowing users to access different features of the application.
    """
    
    def setupUi(self, MainScreen):
        """
        Set up the user interface for the Main Screen.
        
        Args:
            MainScreen (QMainWindow): The main window to set up
        """
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(1200, 700)
        MainScreen.setWindowIcon(QtGui.QIcon('images/cypress_logo.png'))
        
        # Create central widget
        self.centralwidget = QtWidgets.QWidget(MainScreen)
        self.centralwidget.setObjectName("centralwidget")
        
        # Use grid layout for main layout
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        # Create header section
        self.header_widget = QtWidgets.QWidget(self.centralwidget)
        self.header_widget.setMaximumHeight(100)
        self.header_layout = QtWidgets.QHBoxLayout(self.header_widget)
        
        # Create CYPRESS header label
        self.header_label = QtWidgets.QLabel(self.header_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        self.header_label.setFont(font)
        self.header_label.setObjectName("header_label")
        self.header_label.setText("City of Toronto - Cypress")
        self.header_layout.addWidget(self.header_label)
        
        # Create City of Toronto header label
        self.header_label2 = QtWidgets.QLabel(self.header_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        self.header_label2.setFont(font)
        self.header_label2.setAlignment(QtCore.Qt.AlignRight)
        self.header_label2.setObjectName("header_label2")
        self.header_label2.setText("")
        self.header_layout.addWidget(self.header_label2)
        
        # Add header to main layout
        self.gridLayout.addWidget(self.header_widget, 0, 0, 1, 2)
        
        # Create description label
        self.description_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.description_label.setFont(font)
        self.description_label.setAlignment(QtCore.Qt.AlignCenter)
        self.description_label.setObjectName("description_label")
        self.description_label.setText("Keeping Our City Streets Clean and Safe...")
        self.gridLayout.addWidget(self.description_label, 1, 0, 1, 2)
        
        # Create left panel for navigation options
        self.left_panel = QtWidgets.QWidget(self.centralwidget)
        self.left_panel.setMinimumWidth(300)
        self.left_panel.setMaximumWidth(400)
        self.left_layout = QtWidgets.QVBoxLayout(self.left_panel)
        self.left_layout.setContentsMargins(10, 20, 10, 20)
        self.left_layout.setSpacing(15)
        
        # Admin mode label (only visible in admin mode)
        self.admin_label = QtWidgets.QLabel(self.left_panel)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.admin_label.setFont(font)
        self.admin_label.setText("ADMINISTRATOR MODE")
        self.admin_label.setStyleSheet("color: red;")
        self.admin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.admin_label.setObjectName("admin_label")
        self.left_layout.addWidget(self.admin_label)
        
        # Create navigation buttons with improved styling
        self.report_button = QtWidgets.QRadioButton(self.left_panel)
        self.report_button.setObjectName("report_button")
        self.report_button.setMinimumHeight(40)
        self.report_button.setText("Report a Problem")
        self.report_button.setStyleSheet("""
            QRadioButton {
                background-color: #2ecc71;
                color: white;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QRadioButton:checked {
                background-color: #27ae60;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                margin-left: 5px;
            }
        """)
        self.left_layout.addWidget(self.report_button)
        
        self.suggest_button = QtWidgets.QRadioButton(self.left_panel)
        self.suggest_button.setObjectName("suggest_button")
        self.suggest_button.setMinimumHeight(40)
        self.suggest_button.setText("Suggest")
        self.suggest_button.setStyleSheet("""
            QRadioButton {
                background-color: white;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
            QRadioButton:checked {
                background-color: #f0f0f0;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                margin-left: 5px;
            }
        """)
        self.left_layout.addWidget(self.suggest_button)
        
        self.myReports_button = QtWidgets.QRadioButton(self.left_panel)
        self.myReports_button.setObjectName("myReports_button")
        self.myReports_button.setMinimumHeight(40)
        self.myReports_button.setText("My Reports")
        self.myReports_button.setStyleSheet("""
            QRadioButton {
                background-color: white;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
            QRadioButton:checked {
                background-color: #f0f0f0;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                margin-left: 5px;
            }
        """)
        self.left_layout.addWidget(self.myReports_button)
        
        # Admin-specific buttons
        self.admin_reports_button = QtWidgets.QRadioButton(self.left_panel)
        self.admin_reports_button.setText("Admin Reports")
        self.admin_reports_button.setObjectName("admin_reports_button")
        self.admin_reports_button.setMinimumHeight(40)
        self.admin_reports_button.setStyleSheet("""
            QRadioButton {
                background-color: white;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
            QRadioButton:checked {
                background-color: #f0f0f0;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                margin-left: 5px;
            }
        """)
        self.left_layout.addWidget(self.admin_reports_button)
        
        self.user_management_button = QtWidgets.QRadioButton(self.left_panel)
        self.user_management_button.setText("User Management")
        self.user_management_button.setObjectName("user_management_button")
        self.user_management_button.setMinimumHeight(40)
        self.user_management_button.setStyleSheet("""
            QRadioButton {
                background-color: white;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
            QRadioButton:checked {
                background-color: #f0f0f0;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                margin-left: 5px;
            }
        """)
        self.left_layout.addWidget(self.user_management_button)
        
        self.system_settings_button = QtWidgets.QRadioButton(self.left_panel)
        self.system_settings_button.setText("System Settings")
        self.system_settings_button.setObjectName("system_settings_button")
        self.system_settings_button.setMinimumHeight(40)
        self.system_settings_button.setStyleSheet("""
            QRadioButton {
                background-color: white;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
            QRadioButton:checked {
                background-color: #f0f0f0;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                margin-left: 5px;
            }
        """)
        self.left_layout.addWidget(self.system_settings_button)
        
        # Logout button
        self.logout_button = QtWidgets.QRadioButton(self.left_panel)
        self.logout_button.setText("Logout")
        self.logout_button.setObjectName("logout_button")
        self.logout_button.setMinimumHeight(40)
        self.logout_button.setStyleSheet("""
            QRadioButton {
                background-color: white;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
            QRadioButton:checked {
                background-color: #f0f0f0;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                margin-left: 5px;
            }
        """)
        self.left_layout.addWidget(self.logout_button)
        
        # Quick links section
        self.links_label = QtWidgets.QLabel(self.left_panel)
        self.links_label.setObjectName("links_label")
        self.links_label.setStyleSheet("font-weight: bold; color: #3498db; margin-top: 20px;")
        self.links_label.setText("QUICK LINKS >>")
        self.left_layout.addWidget(self.links_label)
        
        # Add spacer to push everything to the top
        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.left_layout.addItem(spacer)
        
        # Go button to navigate to selected option
        self.go_button = QtWidgets.QPushButton(self.left_panel)
        self.go_button.setText("Go")
        self.go_button.setObjectName("go_button")
        self.go_button.setMinimumHeight(50)
        self.go_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 4px;
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
        self.left_layout.addWidget(self.go_button)
        
        # Add exit button
        self.exit_button = QtWidgets.QPushButton(self.left_panel)
        self.exit_button.setText("Exit Application")
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setMinimumHeight(50)
        self.exit_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 4px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #a93226;
            }
        """)
        self.left_layout.addWidget(self.exit_button)
        
        # Add left panel to main layout
        self.gridLayout.addWidget(self.left_panel, 2, 0, 1, 1)
        
        # Add image to right side
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setPixmap(QtGui.QPixmap("images/cn_tower_pic.jpg"))
        self.image_label.setScaledContents(True)
        self.image_label.setMinimumSize(500, 400)
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 2, 1, 1, 1)
        
        # Set central widget
        MainScreen.setCentralWidget(self.centralwidget)
        
        # Create menubar and statusbar
        self.menubar = QtWidgets.QMenuBar(MainScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        MainScreen.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainScreen)
        self.statusbar.setObjectName("statusbar")
        MainScreen.setStatusBar(self.statusbar)
        
        # Set window title
        MainScreen.setWindowTitle("Cypress")
        QtCore.QMetaObject.connectSlotsByName(MainScreen)
    
    def setUIText(self, MainScreen):
        """
        Set the text for all UI elements.
        
        Args:
            MainScreen (QMainWindow): The main window containing the UI elements
        """
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainScreen = QtWidgets.QMainWindow()
    ui = Ui_MainScreen()
    ui.setupUi(MainScreen)
    MainScreen.show()
    sys.exit(app.exec_())
