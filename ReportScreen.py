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
        
        self.retranslateUi(ReportScreen)
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
        # For main_ui.py compatibility
        self.buttons_container = QtWidgets.QWidget(self.centralwidget)
        self.buttons_container.setObjectName("buttons_container")
        self.buttons_layout = QtWidgets.QHBoxLayout(self.buttons_container)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.buttons_layout.setSpacing(20)
        
        # Spacer to push buttons to the right
        spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons_layout.addItem(spacer)
        
        # Report button (renamed from submit_button for compatibility)
        self.report_button = QtWidgets.QPushButton(self.buttons_container)
        self.report_button.setMinimumSize(QtCore.QSize(180, 50))
        self.report_button.setMaximumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.report_button.setFont(font)
        self.report_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.report_button.setObjectName("report_button")
        self.buttons_layout.addWidget(self.report_button)
        
        # Cancel button
        self.cancel_button = QtWidgets.QPushButton(self.buttons_container)
        self.cancel_button.setMinimumSize(QtCore.QSize(180, 50))
        self.cancel_button.setMaximumSize(QtCore.QSize(180, 50))
        self.cancel_button.setFont(font)
        self.cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_button.setObjectName("cancel_button")
        self.buttons_layout.addWidget(self.cancel_button)
        
        # Add buttons container to main layout
        self.mainLayout.addWidget(self.buttons_container)
        
        # Create submit_button as an alias to report_button for new code
        self.submit_button = self.report_button
    
    def retranslateUi(self, ReportScreen):
        """
        Set the text for UI elements.
        
        Args:
            ReportScreen (QMainWindow): The main window containing the UI elements
        """
        _translate = QtCore.QCoreApplication.translate
        ReportScreen.setWindowTitle(_translate("ReportScreen", "Report an Issue"))
        self.address_label.setText(_translate("ReportScreen", "Address:"))
        self.problems_label.setText(_translate("ReportScreen", "What's the problem?"))
        
        # Problem options
        self.utility_failures_button.setText(_translate("ReportScreen", "Utility Failures"))
        self.potholes_button.setText(_translate("ReportScreen", "Potholes"))
        self.vandalism_button.setText(_translate("ReportScreen", "City Property Vandalism"))
        self.erroded_streets_button.setText(_translate("ReportScreen", "Eroded Streets"))
        self.tree_collapse_button.setText(_translate("ReportScreen", "Tree Collapse"))
        self.flooded_streets_button.setText(_translate("ReportScreen", "Flooded Streets"))
        self.mould_button.setText(_translate("ReportScreen", "Mould and Spore Growth"))
        self.garbage_button.setText(_translate("ReportScreen", "Garbage or Road Blocking Objects"))
        
        self.description_label.setText(_translate("ReportScreen", "Description"))
        self.attachment_label.setText(_translate("ReportScreen", "Attach Image:"))
        self.browse_button.setText(_translate("ReportScreen", "Browse Files"))
        self.cancel_button.setText(_translate("ReportScreen", "Cancel"))
        self.report_button.setText(_translate("ReportScreen", "Report"))
    
    def retranslateUi_french(self, ReportScreen):
        """
        Set the text for UI elements in French.
        
        Args:
            ReportScreen (QMainWindow): The main window containing the UI elements
        """
        _translate = QtCore.QCoreApplication.translate
        ReportScreen.setWindowTitle(_translate("ReportScreen", "Signaler un problème"))
        self.address_label.setText(_translate("ReportScreen", "Addresse:"))
        self.problems_label.setText(_translate("ReportScreen", "PROBLÈMES SUR LE SITE:"))
        self.utility_failures_button.setText(_translate("ReportScreen", "Pannes de L'utilitaire"))
        self.potholes_button.setText(_translate("ReportScreen", "Nids-de-poule"))
        self.erroded_streets_button.setText(_translate("ReportScreen", "Rues Érodées"))
        self.vandalism_button.setText(_translate("ReportScreen", "Vandalisme de propriété de la ville"))
        self.tree_collapse_button.setText(_translate("ReportScreen", "Effondrement d'arbre"))
        self.flooded_streets_button.setText(_translate("ReportScreen", "Rues inondées"))
        self.mould_button.setText(_translate("ReportScreen", "Croissance de moisissures et de spores"))
        self.garbage_button.setText(_translate("ReportScreen", "Déchets ou autres objets bloquant la route"))
        self.description_label.setText(_translate("ReportScreen", "Description:"))
        self.attachment_label.setText(_translate("ReportScreen", "Joindre une Image:"))
        self.browse_button.setText(_translate("ReportScreen", "Parcourir"))
        self.report_button.setText(_translate("ReportScreen", "Rapport"))
        self.cancel_button.setText(_translate("ReportScreen", "Annuler"))


class MyReportScreen(QtWidgets.QMainWindow, Ui_ReportScreen):
    """
    Functional implementation of the Report Screen.
    
    This class extends the UI definition with actual functionality, handling
    user interactions and connecting signals to slots.
    """
    
    def __init__(self, parent=None):
        """
        Initialize the Report Screen with functionality.
        
        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
        """
        super(MyReportScreen, self).__init__(parent)
        self.setupUi(self)
        
        # Connect signals to slots
        self.cancel_button.clicked.connect(self.cancel_clicked)
        self.submit_button.clicked.connect(self.submit_report)
        self.map_button.clicked.connect(self.open_map_dialog)
    
    def submit_report(self):
        """Handle the submission of a report."""
        # Validate inputs
        if not self.validate_inputs():
            return
        
        # Get selected problem
        problem = self.get_selected_problem()
        
        # Here you would typically save the report to a database
        # For now, just show a success message
        QtWidgets.QMessageBox.information(
            self,
            "Report Submitted",
            f"Thank you for your report about '{problem}' at {self.address_input.text()}. \n\n"
            "Your report has been submitted successfully and will be reviewed by our team."
        )
        
        # Go back to the main screen instead of just closing
        self.hide()
        from main_ui import MyMainScreen
        self.next = MyMainScreen()
        self.next.show()
    
    def cancel_clicked(self):
        """Return to the main screen when cancel is clicked."""
        self.hide()
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
