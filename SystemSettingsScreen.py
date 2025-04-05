from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QTabWidget, QFormLayout, QLineEdit, QComboBox, QCheckBox, QMessageBox
from PyQt5.QtWidgets import QSpinBox, QColorDialog, QFileDialog, QGroupBox, QRadioButton
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtGui import QFont, QColor

import json
import os
import datetime

class Ui_SystemSettingsScreen(object):
    """UI definition for the System Settings Screen."""
    
    def setupUi(self, SystemSettingsScreen):
        """Set up the UI components for the System Settings Screen."""
        SystemSettingsScreen.setObjectName("SystemSettingsScreen")
        SystemSettingsScreen.resize(1000, 700)
        
        # Create central widget
        self.centralwidget = QWidget(SystemSettingsScreen)
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
        self.title_label = QLabel("System Settings")
        title_font = QFont()
        title_font.setFamily("Arial")
        title_font.setPointSize(24)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.header_layout.addWidget(self.title_label)
        
        # Add description label
        self.description_label = QLabel("Configure application settings and preferences")
        desc_font = QFont()
        desc_font.setFamily("Arial")
        desc_font.setPointSize(12)
        self.description_label.setFont(desc_font)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.header_layout.addWidget(self.description_label)
        
        # Add header to main layout
        self.main_layout.addWidget(self.header_widget)
        
        # Create tab widget for settings categories
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName("tab_widget")
        
        # Create general settings tab
        self.general_tab = QWidget()
        self.general_tab.setObjectName("general_tab")
        self.general_layout = QVBoxLayout(self.general_tab)
        
        # Create general settings form
        self.general_form = QFormLayout()
        self.general_form.setSpacing(15)
        
        # Application name setting
        self.app_name_input = QLineEdit(self.general_tab)
        self.app_name_input.setText("Cypress - City of Toronto")
        self.general_form.addRow("Application Name:", self.app_name_input)
        
        # Language setting
        self.language_combo = QComboBox(self.general_tab)
        self.language_combo.addItems(["English", "French"])
        self.general_form.addRow("Language:", self.language_combo)
        
        # Theme setting
        self.theme_combo = QComboBox(self.general_tab)
        self.theme_combo.addItems(["Light", "Dark", "System"])
        self.general_form.addRow("Theme:", self.theme_combo)
        
        # Auto-save setting
        self.autosave_check = QCheckBox(self.general_tab)
        self.autosave_check.setChecked(True)
        self.general_form.addRow("Enable Auto-Save:", self.autosave_check)
        
        # Add form to general tab
        self.general_layout.addLayout(self.general_form)
        self.general_layout.addStretch()
        
        # Add general tab to tab widget
        self.tab_widget.addTab(self.general_tab, "General")
        
        # Create appearance tab
        self.appearance_tab = QWidget()
        self.appearance_tab.setObjectName("appearance_tab")
        self.appearance_layout = QVBoxLayout(self.appearance_tab)
        
        # Create appearance form
        self.appearance_form = QFormLayout()
        self.appearance_form.setSpacing(15)
        
        # Font size setting
        self.font_size_spin = QSpinBox(self.appearance_tab)
        self.font_size_spin.setRange(8, 24)
        self.font_size_spin.setValue(12)
        self.appearance_form.addRow("Font Size:", self.font_size_spin)
        
        # Primary color setting
        self.primary_color_button = QPushButton(self.appearance_tab)
        self.primary_color_button.setText("Select Color")
        self.primary_color = QColor("#3498db")  # Default blue
        self.update_color_button(self.primary_color_button, self.primary_color)
        self.appearance_form.addRow("Primary Color:", self.primary_color_button)
        
        # Secondary color setting
        self.secondary_color_button = QPushButton(self.appearance_tab)
        self.secondary_color_button.setText("Select Color")
        self.secondary_color = QColor("#2ecc71")  # Default green
        self.update_color_button(self.secondary_color_button, self.secondary_color)
        self.appearance_form.addRow("Secondary Color:", self.secondary_color_button)
        
        # Add form to appearance tab
        self.appearance_layout.addLayout(self.appearance_form)
        self.appearance_layout.addStretch()
        
        # Add appearance tab to tab widget
        self.tab_widget.addTab(self.appearance_tab, "Appearance")
        
        # Create data tab
        self.data_tab = QWidget()
        self.data_tab.setObjectName("data_tab")
        self.data_layout = QVBoxLayout(self.data_tab)
        
        # Create data form
        self.data_form = QFormLayout()
        self.data_form.setSpacing(15)
        
        # Data directory setting
        self.data_dir_layout = QHBoxLayout()
        self.data_dir_input = QLineEdit(self.data_tab)
        self.data_dir_input.setText(os.getcwd())
        self.data_dir_layout.addWidget(self.data_dir_input)
        
        self.browse_button = QPushButton("Browse")
        self.browse_button.setMaximumWidth(100)
        self.data_dir_layout.addWidget(self.browse_button)
        
        self.data_form.addRow("Data Directory:", self.data_dir_layout)
        
        # Backup settings
        self.backup_check = QCheckBox(self.data_tab)
        self.backup_check.setChecked(True)
        self.data_form.addRow("Enable Automatic Backups:", self.backup_check)
        
        self.backup_interval_spin = QSpinBox(self.data_tab)
        self.backup_interval_spin.setRange(1, 30)
        self.backup_interval_spin.setValue(7)
        self.data_form.addRow("Backup Interval (days):", self.backup_interval_spin)
        
        # Add data management buttons
        self.backup_now_button = QPushButton("Backup Now")
        self.data_form.addRow("", self.backup_now_button)
        
        self.restore_button = QPushButton("Restore from Backup")
        self.data_form.addRow("", self.restore_button)
        
        self.reset_button = QPushButton("Reset to Default Settings")
        self.data_form.addRow("", self.reset_button)
        
        # Add form to data tab
        self.data_layout.addLayout(self.data_form)
        self.data_layout.addStretch()
        
        # Add data tab to tab widget
        self.tab_widget.addTab(self.data_tab, "Data & Backup")
        
        # Add tab widget to main layout
        self.main_layout.addWidget(self.tab_widget)
        
        # Create button layout
        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(10)
        
        # Add save button
        self.save_button = QPushButton("Save Settings")
        self.save_button.setMinimumHeight(40)
        self.button_layout.addWidget(self.save_button)
        
        # Add spacer
        self.button_layout.addStretch()
        
        # Add back button
        self.back_button = QPushButton("Back to Main")
        self.back_button.setMinimumHeight(40)
        self.button_layout.addWidget(self.back_button)
        
        # Add button layout to main layout
        self.main_layout.addLayout(self.button_layout)
        
        # Set central widget
        SystemSettingsScreen.setCentralWidget(self.centralwidget)
        
        # Set text for UI elements
        self.set_text(SystemSettingsScreen)
        
        # Apply modern styling
        self.apply_styling()
    
    def set_text(self, SystemSettingsScreen):
        """Set the text for UI elements."""
        SystemSettingsScreen.setWindowTitle("Cypress - System Settings")
        self.title_label.setText("System Settings")
        self.description_label.setText("Configure application settings and preferences")
        self.tab_widget.setTabText(0, "General")
        self.tab_widget.setTabText(1, "Appearance")
        self.tab_widget.setTabText(2, "Data & Backup")
        self.save_button.setText("Save Settings")
        self.back_button.setText("Back to Main")
    
    def update_color_button(self, button, color):
        """Update the color button with the selected color."""
        button.setStyleSheet(
            f"background-color: {color.name()}; color: {'white' if color.lightness() < 128 else 'black'};"
        )
    
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
        
        self.save_button.setStyleSheet(button_style)
        self.back_button.setStyleSheet(button_style)
        self.browse_button.setStyleSheet(button_style)
        
        # Set tab widget style
        tab_style = """
            QTabWidget::pane {
                border: 1px solid #dcdcdc;
                border-radius: 5px;
                background-color: #ffffff;
                padding: 10px;
            }
            QTabBar::tab {
                background-color: #f0f0f0;
                border: 1px solid #dcdcdc;
                border-bottom: none;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                padding: 8px 15px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: #ffffff;
                border-bottom: 1px solid #ffffff;
            }
            QTabBar::tab:hover {
                background-color: #e0e0e0;
            }
        """
        self.tab_widget.setStyleSheet(tab_style)


class SystemSettingsScreen(QMainWindow, Ui_SystemSettingsScreen):
    """Functional implementation of the System Settings Screen."""
    
    def __init__(self):
        """Initialize the System Settings Screen with functionality."""
        super().__init__()
        self.setupUi(self)
        
        # Initialize settings
        self.settings = QSettings("CityOfToronto", "Cypress")
        
        # Connect button signals to slots
        self.back_button.clicked.connect(self.back_clicked)
        self.save_button.clicked.connect(self.save_settings)
        self.primary_color_button.clicked.connect(self.select_primary_color)
        self.secondary_color_button.clicked.connect(self.select_secondary_color)
        self.browse_button.clicked.connect(self.browse_data_directory)
        self.backup_now_button.clicked.connect(self.backup_now)
        self.restore_button.clicked.connect(self.restore_from_backup)
        self.reset_button.clicked.connect(self.reset_settings)
        
        # Load settings
        self.load_settings()
    
    def load_settings(self):
        """Load settings from QSettings."""
        # General settings
        self.app_name_input.setText(self.settings.value("general/appName", "Cypress - City of Toronto"))
        self.language_combo.setCurrentText(self.settings.value("general/language", "English"))
        self.theme_combo.setCurrentText(self.settings.value("general/theme", "Light"))
        self.autosave_check.setChecked(self.settings.value("general/autosave", True, type=bool))
        
        # Appearance settings
        self.font_size_spin.setValue(self.settings.value("appearance/fontSize", 12, type=int))
        
        primary_color = self.settings.value("appearance/primaryColor", "#3498db")
        self.primary_color = QColor(primary_color)
        self.update_color_button(self.primary_color_button, self.primary_color)
        
        secondary_color = self.settings.value("appearance/secondaryColor", "#2ecc71")
        self.secondary_color = QColor(secondary_color)
        self.update_color_button(self.secondary_color_button, self.secondary_color)
        
        # Data settings
        self.data_dir_input.setText(self.settings.value("data/directory", os.getcwd()))
        self.backup_check.setChecked(self.settings.value("data/autoBackup", True, type=bool))
        self.backup_interval_spin.setValue(self.settings.value("data/backupInterval", 7, type=int))
    
    def save_settings(self):
        """Save settings to QSettings."""
        # General settings
        self.settings.setValue("general/appName", self.app_name_input.text())
        self.settings.setValue("general/language", self.language_combo.currentText())
        self.settings.setValue("general/theme", self.theme_combo.currentText())
        self.settings.setValue("general/autosave", self.autosave_check.isChecked())
        
        # Appearance settings
        self.settings.setValue("appearance/fontSize", self.font_size_spin.value())
        self.settings.setValue("appearance/primaryColor", self.primary_color.name())
        self.settings.setValue("appearance/secondaryColor", self.secondary_color.name())
        
        # Data settings
        self.settings.setValue("data/directory", self.data_dir_input.text())
        self.settings.setValue("data/autoBackup", self.backup_check.isChecked())
        self.settings.setValue("data/backupInterval", self.backup_interval_spin.value())
        
        # Sync settings to disk
        self.settings.sync()
        
        # Show success message
        QMessageBox.information(
            self,
            "Settings Saved",
            "Your settings have been saved successfully."
        )
    
    def select_primary_color(self):
        """Open color dialog to select primary color."""
        color = QColorDialog.getColor(self.primary_color, self, "Select Primary Color")
        if color.isValid():
            self.primary_color = color
            self.update_color_button(self.primary_color_button, color)
    
    def select_secondary_color(self):
        """Open color dialog to select secondary color."""
        color = QColorDialog.getColor(self.secondary_color, self, "Select Secondary Color")
        if color.isValid():
            self.secondary_color = color
            self.update_color_button(self.secondary_color_button, color)
    
    def browse_data_directory(self):
        """Open file dialog to select data directory."""
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Data Directory",
            self.data_dir_input.text(),
            QFileDialog.ShowDirsOnly
        )
        if directory:
            self.data_dir_input.setText(directory)
    
    def backup_now(self):
        """Create a backup of application data."""
        try:
            # Create backup directory if it doesn't exist
            backup_dir = os.path.join(self.data_dir_input.text(), "backups")
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            
            # Create backup filename with timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = os.path.join(backup_dir, f"cypress_backup_{timestamp}")
            
            # Create backup of users.txt
            if os.path.exists("users.txt"):
                with open("users.txt", "r") as src, open(f"{backup_file}_users.txt", "w") as dst:
                    dst.write(src.read())
            
            # Create backup of reports.json
            if os.path.exists("reports.json"):
                with open("reports.json", "r") as src, open(f"{backup_file}_reports.json", "w") as dst:
                    dst.write(src.read())
            
            # Show success message
            QMessageBox.information(
                self,
                "Backup Created",
                f"Backup created successfully in:\n{backup_dir}"
            )
        except Exception as e:
            # Show error message
            QMessageBox.critical(
                self,
                "Backup Failed",
                f"Failed to create backup: {str(e)}"
            )
    
    def restore_from_backup(self):
        """Restore data from a backup."""
        # Open file dialog to select backup file
        backup_dir = os.path.join(self.data_dir_input.text(), "backups")
        if not os.path.exists(backup_dir):
            QMessageBox.warning(
                self,
                "No Backups",
                "No backup directory found. Please create a backup first."
            )
            return
        
        # Show warning message
        reply = QMessageBox.warning(
            self,
            "Restore from Backup",
            "Restoring from backup will overwrite current data. Continue?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Implement restore functionality
            QMessageBox.information(
                self,
                "Restore from Backup",
                "This feature is not fully implemented yet."
            )
    
    def reset_settings(self):
        """Reset settings to default values."""
        # Show confirmation dialog
        reply = QMessageBox.question(
            self,
            "Reset Settings",
            "Are you sure you want to reset all settings to default values?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Clear all settings
            self.settings.clear()
            
            # Reload settings with defaults
            self.load_settings()
            
            # Show success message
            QMessageBox.information(
                self,
                "Settings Reset",
                "All settings have been reset to default values."
            )
    
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
