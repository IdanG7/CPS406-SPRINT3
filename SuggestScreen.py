#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Suggest Screen Module

This module provides the UI for suggesting solutions to reported problems.
It allows citizens to view reported issues, suggest solutions, and prioritize
problems by liking them.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from SuggestPopUp import SuggestPopUp


class Ui_SuggestScreen(object):
    """
    UI class for the Suggest Screen.
    
    This class defines the user interface elements for the suggestion screen,
    allowing users to interact with reported problems and propose solutions.
    """
    
    def setupUi(self, SuggestScreen):
        """
        Set up the user interface for the Suggest Screen.
        
        Args:
            SuggestScreen (QMainWindow): The main window to set up
        """
        SuggestScreen.setObjectName("SuggestScreen")
        SuggestScreen.resize(811, 466)
        SuggestScreen.setWindowIcon(QtGui.QIcon('images/cypress_logo.png'))
        
        # Create central widget
        self.centralwidget = QtWidgets.QWidget(SuggestScreen)
        self.centralwidget.setObjectName("centralwidget")
        
        # Set up main layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self._setup_header()
        self._setup_description()
        self._setup_scroll_area()
        self._setup_buttons()
        
        SuggestScreen.setCentralWidget(self.centralwidget)
        
        # Set up menu and status bar
        self._setup_menu_and_status_bar(SuggestScreen)
        
        self.retranslateUi(SuggestScreen)
        QtCore.QMetaObject.connectSlotsByName(SuggestScreen)
    
    def _setup_header(self):
        """Set up the header section with logo and title."""
        # Create frame for header labels
        self.labelFrame = QtWidgets.QFrame(self.centralwidget)
        self.labelFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.labelFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelFrame.setLineWidth(1)
        self.labelFrame.setObjectName("labelFrame")
        self.verticalLayout.addWidget(self.labelFrame)
        
        # Create layout for header labels
        self.labelLayout = QtWidgets.QHBoxLayout(self.labelFrame)
        self.labelLayout.setObjectName("labelLayout")
        
        # Create header font
        header_font = QtGui.QFont()
        header_font.setFamily("Gubbi")
        header_font.setPointSize(15)
        header_font.setBold(True)
        header_font.setWeight(75)
        
        # Create left header label (CYPRESS)
        self.header_label = QtWidgets.QLabel(self.labelFrame)
        self.header_label.setFont(header_font)
        self.header_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.header_label.setIndent(-1)
        self.header_label.setObjectName("header_label")
        self.labelLayout.addWidget(self.header_label)
        
        # Create right header label (City of Toronto)
        self.header_label2 = QtWidgets.QLabel(self.labelFrame)
        self.header_label2.setFont(header_font)
        self.header_label2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.header_label2.setIndent(-1)
        self.header_label2.setObjectName("header_label2")
        self.labelLayout.addWidget(self.header_label2)
    
    def _setup_description(self):
        """Set up the description section."""
        # Create description label
        self.description_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.description_label.setFont(font)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.verticalLayout.addWidget(self.description_label)
    
    def _setup_scroll_area(self):
        """Set up the scrollable area for displaying problems."""
        # Create scroll area
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        
        # Create scroll area content widget
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 810, 276))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        # Create layout for scroll area content
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        # Set scroll area widget
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
    
    def _setup_buttons(self):
        """Set up the submit and cancel buttons."""
        # Create button font
        button_font = QtGui.QFont()
        button_font.setPointSize(11)
        
        # Create submit button
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setObjectName("submit_button")
        self.submit_button.setFont(button_font)
        self.submit_button.setMinimumHeight(40)
        self.submit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.submit_button)
        
        # Create cancel button
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setFont(button_font)
        self.cancel_button.setMinimumHeight(40)
        self.cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.cancel_button)
    
    def _setup_menu_and_status_bar(self, SuggestScreen):
        """Set up the menu bar and status bar."""
        # Create menu bar
        self.menubar = QtWidgets.QMenuBar(SuggestScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 22))
        self.menubar.setObjectName("menubar")
        SuggestScreen.setMenuBar(self.menubar)
        
        # Create status bar
        self.statusbar = QtWidgets.QStatusBar(SuggestScreen)
        self.statusbar.setObjectName("statusbar")
        SuggestScreen.setStatusBar(self.statusbar)
    
    def retranslateUi(self, SuggestScreen):
        """
        Set the text for UI elements.
        
        Args:
            SuggestScreen (QMainWindow): The main window containing the UI elements
        """
        _translate = QtCore.QCoreApplication.translate
        SuggestScreen.setWindowTitle(_translate("SuggestScreen", "Cypress - Suggest Solutions"))
        self.header_label.setText(_translate("SuggestScreen", "CYPRESS"))
        self.header_label2.setText(_translate("SuggestScreen", "City of Toronto"))
        self.description_label.setText(_translate("SuggestScreen", 
            "Suggest solutions to reported problems and assign priority by liking a problem"))
        self.submit_button.setText(_translate("SuggestScreen", "Submit"))
        self.cancel_button.setText(_translate("SuggestScreen", "Cancel"))


class MySuggestScreen(QtWidgets.QMainWindow):
    """
    Functional implementation of the Suggest Screen.
    
    This class extends the UI definition with actual functionality, handling
    user interactions and connecting signals to slots.
    """
    
    def __init__(self, parent=None, reported_problems=None):
        """
        Initialize the Suggest Screen with functionality.
        
        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
            reported_problems (list, optional): List of reported problems to display.
                If None, dummy data will be used.
        """
        super(MySuggestScreen, self).__init__(parent)
        self.ui = Ui_SuggestScreen()
        self.ui.setupUi(self)
        
        # Initialize variables
        self.selected_problems = []
        self.suggestions = {}
        
        # Use provided problems or get dummy problems
        self.problems = reported_problems if reported_problems else self._get_dummy_problems()
        
        # Populate the problem list
        self._populate_problem_list()
        
        # Connect buttons to actions
        self.ui.submit_button.clicked.connect(self.submit_suggestions)
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)
    
    def _get_dummy_problems(self):
        """
        Get dummy problem data for testing.
        
        Returns:
            list: A list of dummy problem dictionaries
        """
        return [
            {
                "id": 1,
                "problem_type": "Pothole",
                "address": "123 Main St, Toronto, ON",
                "date_reported": "2023-03-15",
                "description": "Large pothole in the middle of the road causing traffic hazards."
            },
            {
                "id": 2,
                "problem_type": "Broken Streetlight",
                "address": "456 Elm St, Toronto, ON",
                "date_reported": "2023-03-14",
                "description": "Streetlight is flickering and sometimes goes out completely at night."
            },
            {
                "id": 3,
                "problem_type": "Graffiti",
                "address": "789 Oak Ave, Toronto, ON",
                "date_reported": "2023-03-13",
                "description": "Offensive graffiti on the side of the public library building."
            }
        ]
    
    def _populate_problem_list(self):
        """Populate the scroll area with problem cards."""
        # Clear any existing content
        while self.ui.verticalLayout_2.count():
            item = self.ui.verticalLayout_2.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Add problem cards
        for problem in self.problems:
            self._create_problem_card(problem)
    
    def _create_problem_card(self, problem):
        """
        Create and add a card for a problem to the scroll area.
        
        Args:
            problem (dict): Problem data to display
        """
        # Create card frame
        card = QtWidgets.QFrame()
        card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        card.setFrameShadow(QtWidgets.QFrame.Raised)
        card.setStyleSheet("QFrame { background-color: #f8f9fa; border-radius: 8px; margin: 5px; }")
        
        # Create layout for card
        card_layout = QtWidgets.QVBoxLayout(card)
        
        # Create header with problem type and date
        header_layout = QtWidgets.QHBoxLayout()
        
        problem_type = QtWidgets.QLabel(problem["problem_type"])
        problem_type.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        header_layout.addWidget(problem_type)
        
        spacer = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        header_layout.addItem(spacer)
        
        date = QtWidgets.QLabel(f"Reported: {problem['date_reported']}")
        date.setFont(QtGui.QFont("Arial", 10))
        header_layout.addWidget(date)
        
        card_layout.addLayout(header_layout)
        
        # Add address
        address = QtWidgets.QLabel(problem["address"])
        address.setFont(QtGui.QFont("Arial", 11))
        card_layout.addWidget(address)
        
        # Add description
        description = QtWidgets.QLabel(problem["description"])
        description.setWordWrap(True)
        card_layout.addWidget(description)
        
        # Add actions layout
        actions_layout = QtWidgets.QHBoxLayout()
        
        # Add like button
        like_button = QtWidgets.QPushButton("👍 Like")
        like_button.setObjectName(f"like_button_{problem['id']}")
        like_button.clicked.connect(lambda checked, pid=problem["id"]: self._toggle_like(pid))
        like_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        actions_layout.addWidget(like_button)
        
        # Add suggest button
        suggest_button = QtWidgets.QPushButton("💡 Suggest Solution")
        suggest_button.setObjectName(f"suggest_button_{problem['id']}")
        suggest_button.clicked.connect(lambda checked, p=problem: self._open_suggest_popup(p))
        suggest_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        actions_layout.addWidget(suggest_button)
        
        # Add actions to card
        card_layout.addLayout(actions_layout)
        
        # Add card to main layout
        self.ui.verticalLayout_2.addWidget(card)
    
    def _toggle_like(self, problem_id):
        """
        Toggle the like status for a problem.
        
        Args:
            problem_id (int): ID of the problem to toggle like status
        """
        sender = self.sender()
        
        if problem_id in self.selected_problems:
            # Unlike
            self.selected_problems.remove(problem_id)
            sender.setText("👍 Like")
            sender.setStyleSheet("")
        else:
            # Like
            self.selected_problems.append(problem_id)
            sender.setText("👍 Liked")
            sender.setStyleSheet("background-color: #e0f7fa;")
    
    def _open_suggest_popup(self, problem):
        """
        Open a popup dialog to suggest a solution for a problem.
        
        Args:
            problem (dict): Problem data for which to suggest a solution
        """
        popup = SuggestPopUp(problem, self)
        popup.exec_()
    
    def submit_suggestions(self):
        """Submit all suggestions and likes."""
        if not self.selected_problems:
            QtWidgets.QMessageBox.warning(
                self,
                "No Selection",
                "Please like at least one problem to prioritize it."
            )
            return
        
        message = f"You have prioritized {len(self.selected_problems)} problems."
        
        QtWidgets.QMessageBox.information(
            self,
            "Suggestions Submitted",
            message + "\n\nThank you for your input to help improve your community!"
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


# For standalone testing
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # Apply stylesheet if available
    try:
        with open("modern_style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except (FileNotFoundError, IOError):
        pass
    
    suggest_screen = MySuggestScreen()
    suggest_screen.show()
    sys.exit(app.exec_())
