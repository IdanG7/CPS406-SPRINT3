#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Suggest Screen Module

This module provides the UI for suggesting solutions to reported problems.
It allows citizens to view reported issues, suggest solutions, and prioritize
problems by liking them.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime


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
        SuggestScreen.resize(900, 700)
        SuggestScreen.setWindowIcon(QtGui.QIcon('images/cypress_logo.png'))
        SuggestScreen.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
        """)
        
        # Create central widget
        self.centralwidget = QtWidgets.QWidget(SuggestScreen)
        self.centralwidget.setObjectName("centralwidget")
        
        # Set up main layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(30, 20, 30, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Create a stacked widget to switch between problem list and suggestion view
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        
        # Create the problem list page
        self.problemListPage = QtWidgets.QWidget()
        self.problemListPage.setObjectName("problemListPage")
        self.problemListLayout = QtWidgets.QVBoxLayout(self.problemListPage)
        self.problemListLayout.setContentsMargins(0, 0, 0, 0)
        self.problemListLayout.setSpacing(20)
        
        # Set up the problem list UI components
        self._setup_header(self.problemListPage, self.problemListLayout)
        self._setup_description(self.problemListPage, self.problemListLayout)
        self._setup_scroll_area(self.problemListPage, self.problemListLayout)
        self._setup_buttons(self.problemListPage, self.problemListLayout)
        
        # Add problem list page to stacked widget
        self.stackedWidget.addWidget(self.problemListPage)
        
        # Create the suggestion form page
        self.suggestionPage = QtWidgets.QWidget()
        self.suggestionPage.setObjectName("suggestionPage")
        self.suggestionLayout = QtWidgets.QVBoxLayout(self.suggestionPage)
        self.suggestionLayout.setContentsMargins(0, 0, 0, 0)
        self.suggestionLayout.setSpacing(20)
        
        # Set up the suggestion form UI components
        self._setup_suggestion_form(self.suggestionPage, self.suggestionLayout)
        
        # Add suggestion page to stacked widget
        self.stackedWidget.addWidget(self.suggestionPage)
        
        # Add stacked widget to main layout
        self.verticalLayout.addWidget(self.stackedWidget)
        
        SuggestScreen.setCentralWidget(self.centralwidget)
        
        # Set up menu and status bar
        self._setup_menu_and_status_bar(SuggestScreen)
        
        self.set_text(SuggestScreen)
        QtCore.QMetaObject.connectSlotsByName(SuggestScreen)
    
    def _setup_header(self, parent, layout):
        """Set up the header section with logo and title."""
        # Create header widget
        self.header_widget = QtWidgets.QWidget(parent)
        self.header_widget.setMaximumHeight(100)
        self.header_layout = QtWidgets.QVBoxLayout(self.header_widget)
        self.header_layout.setContentsMargins(10, 10, 10, 10)
        
        # Create title label
        self.header_label = QtWidgets.QLabel(self.header_widget)
        title_font = QtGui.QFont()
        title_font.setFamily("Arial")
        title_font.setPointSize(40)
        title_font.setBold(True)
        self.header_label.setFont(title_font)
        self.header_label.setStyleSheet("color: #2c3e50;")
        self.header_label.setAlignment(QtCore.Qt.AlignCenter)
        self.header_label.setObjectName("header_label")
        self.header_layout.addWidget(self.header_label)
        
        # Add header to provided layout
        layout.addWidget(self.header_widget)
    
    def _setup_description(self, parent, layout):
        """Set up the description section."""
        # Create description label
        self.description_label = QtWidgets.QLabel(parent)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.description_label.setFont(font)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        layout.addWidget(self.description_label)
    
    def _setup_scroll_area(self, parent, layout):
        """Set up the scrollable area for displaying problems."""
        # Create scroll area
        self.scrollArea = QtWidgets.QScrollArea(parent)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        
        # Create scroll area content widget
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 810, 276))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        # Create layout for scroll area content
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        # Add spacer at the end to push content to the top
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem)
        
        # Set the widget for the scroll area
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        layout.addWidget(self.scrollArea)
    
    def _setup_buttons(self, parent, layout):
        """Set up the submit and cancel buttons."""
        # Create button layout
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setSpacing(20)
        
        # Create submit button
        self.submit_button = QtWidgets.QPushButton(parent)
        self.submit_button.setMinimumSize(QtCore.QSize(150, 50))
        self.submit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
            QPushButton:pressed {
                background-color: #27ae60;
            }
        """)
        self.submit_button.setObjectName("submit_button")
        self.button_layout.addWidget(self.submit_button)
        
        # Create cancel button
        self.cancel_button = QtWidgets.QPushButton(parent)
        self.cancel_button.setMinimumSize(QtCore.QSize(150, 50))
        self.cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #e74c3c;
            }
        """)
        self.cancel_button.setObjectName("cancel_button")
        self.button_layout.addWidget(self.cancel_button)
        
        # Add button layout to main layout
        layout.addLayout(self.button_layout)
    
    def _setup_suggestion_form(self, parent, layout):
        """Set up the suggestion form UI."""
        # Add header
        suggestion_header = QtWidgets.QLabel(parent)
        suggestion_header.setText("CYPRESS                                                                                  City of Toronto")
        suggestion_header.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(suggestion_header)
        
        # Add title
        suggestion_title = QtWidgets.QLabel(parent)
        title_font = QtGui.QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        suggestion_title.setFont(title_font)
        suggestion_title.setText("Suggest a solution for this reported problem")
        suggestion_title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(suggestion_title)
        
        # Add problem details frame
        self.problem_details_frame = QtWidgets.QFrame(parent)
        self.problem_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.problem_details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        problem_details_layout = QtWidgets.QVBoxLayout(self.problem_details_frame)
        
        # Problem type label
        self.problem_type_label = QtWidgets.QLabel(self.problem_details_frame)
        self.problem_type_label.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        problem_details_layout.addWidget(self.problem_type_label)
        
        # Address label
        self.address_label = QtWidgets.QLabel(self.problem_details_frame)
        self.address_label.setFont(QtGui.QFont("Arial", 12))
        problem_details_layout.addWidget(self.address_label)
        
        # Description label
        self.description_label_2 = QtWidgets.QLabel(self.problem_details_frame)
        self.description_label_2.setFont(QtGui.QFont("Arial", 12))
        self.description_label_2.setWordWrap(True)
        problem_details_layout.addWidget(self.description_label_2)
        
        # Date label
        self.date_label = QtWidgets.QLabel(self.problem_details_frame)
        self.date_label.setFont(QtGui.QFont("Arial", 12))
        problem_details_layout.addWidget(self.date_label)
        
        layout.addWidget(self.problem_details_frame)
        
        # Add suggestion text input
        suggestion_input_label = QtWidgets.QLabel(parent)
        suggestion_input_label.setText("Suggest solution:")
        suggestion_input_label.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        layout.addWidget(suggestion_input_label)
        
        self.suggestion_text = QtWidgets.QTextEdit(parent)
        self.suggestion_text.setMinimumHeight(150)
        self.suggestion_text.setPlaceholderText("Enter your suggestion here...")
        layout.addWidget(self.suggestion_text)
        
        # Add buttons
        buttons_layout = QtWidgets.QHBoxLayout()
        
        # Back button
        self.back_button = QtWidgets.QPushButton("Back", parent)
        self.back_button.setMinimumSize(QtCore.QSize(150, 50))
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        buttons_layout.addWidget(self.back_button)
        
        # Submit suggestion button
        self.submit_suggestion_button = QtWidgets.QPushButton("Submit", parent)
        self.submit_suggestion_button.setMinimumSize(QtCore.QSize(150, 50))
        self.submit_suggestion_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
        """)
        buttons_layout.addWidget(self.submit_suggestion_button)
        
        layout.addLayout(buttons_layout)
    
    def _setup_menu_and_status_bar(self, SuggestScreen):
        """Set up the menu bar and status bar."""
        # Create menu bar
        self.menubar = QtWidgets.QMenuBar(SuggestScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        SuggestScreen.setMenuBar(self.menubar)
        
        # Create status bar
        self.statusbar = QtWidgets.QStatusBar(SuggestScreen)
        self.statusbar.setObjectName("statusbar")
        SuggestScreen.setStatusBar(self.statusbar)
    
    def set_text(self, SuggestScreen):
        """
        Set the text for UI elements.
        
        Args:
            SuggestScreen (QMainWindow): The main window containing the UI elements
        """
        SuggestScreen.setWindowTitle("Cypress - Suggest Solutions")
        self.header_label.setText("Cypress - City of Toronto")
        self.description_label.setText("Reported Problems - Please prioritize and suggest solutions")
        self.submit_button.setText("Submit")
        self.cancel_button.setText("Cancel")


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
        """
        super().__init__()
        print("SuggestScreen.py: MySuggestScreen.__init__ called")
        self.ui = Ui_SuggestScreen()
        self.ui.setupUi(self)
        
        # Store parent reference for navigation
        self.parent = parent
        
        # Set window flags to ensure it stays on top
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        
        # Initialize problem collections
        self.problems = reported_problems or []
        self.selected_problems = set()  # Track problems that have been liked
        self.current_problem = None  # Current problem being viewed for suggestion
        
        # Connect button signals to slots
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)
        self.ui.submit_button.clicked.connect(self.submit_suggestions)
        self.ui.back_button.clicked.connect(self.show_problem_list)
        self.ui.submit_suggestion_button.clicked.connect(self.submit_suggestion)
        
        # Populate the problem list
        self._populate_problem_list()
        
        # Start with the problem list view
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def _populate_problem_list(self):
        """Populate the scroll area with problem cards."""
        # Clear any existing widgets
        for i in reversed(range(self.ui.verticalLayout_2.count() - 1)):
            widget = self.ui.verticalLayout_2.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        
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
        card = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents)
        card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        card.setFrameShadow(QtWidgets.QFrame.Raised)
        card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        
        # Create card layout
        card_layout = QtWidgets.QVBoxLayout(card)
        card_layout.setSpacing(10)
        
        # Add problem type header
        problem_type = QtWidgets.QLabel(problem["problem_type"])
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        problem_type.setFont(font)
        card_layout.addWidget(problem_type)
        
        # Add address
        address = QtWidgets.QLabel(f"Address: {problem['address']}")
        address.setFont(QtGui.QFont("Arial", 11))
        card_layout.addWidget(address)
        
        # Add date
        date = QtWidgets.QLabel(f"Reported: {problem['date_reported']}")
        date.setFont(QtGui.QFont("Arial", 9))
        date.setStyleSheet("color: #7f8c8d;")
        card_layout.addWidget(date)
        
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
        suggest_button.clicked.connect(lambda checked, p=problem: self.show_suggestion_form(p))
        suggest_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        actions_layout.addWidget(suggest_button)
        
        # Add actions to card
        card_layout.addLayout(actions_layout)
        
        # Add card to main layout
        self.ui.verticalLayout_2.insertWidget(self.ui.verticalLayout_2.count() - 1, card)
    
    def _toggle_like(self, problem_id):
        """
        Toggle like status for a problem.
        
        Args:
            problem_id: ID of the problem to toggle like status for
        """
        sender = self.sender()
        
        if problem_id in self.selected_problems:
            # Unlike
            self.selected_problems.remove(problem_id)
            sender.setText("👍 Like")
            sender.setStyleSheet("")
        else:
            # Like
            self.selected_problems.add(problem_id)
            sender.setText("👍 Liked")
            sender.setStyleSheet("background-color: #e0f7fa;")
    
    def show_suggestion_form(self, problem):
        """
        Switch to the suggestion form view for a specific problem.
        
        Args:
            problem (dict): Problem data to suggest a solution for
        """
        print(f"SuggestScreen.py: show_suggestion_form called for problem {problem.get('id', 'unknown')}")
        # Store the current problem
        self.current_problem = problem
        
        # Fill in the problem details
        self.ui.problem_type_label.setText(f"Problem Type: {problem.get('problem_type', 'Unknown')}")
        self.ui.address_label.setText(f"Address: {problem.get('address', 'Unknown')}")
        self.ui.description_label_2.setText(f"Description: {problem.get('description', 'Unknown')}")
        date_str = problem.get('date_reported', 'Unknown')
        self.ui.date_label.setText(f"Date Reported: {date_str}")
        
        # Clear any previous input in the suggestion text box
        self.ui.suggestion_text.clear()
        
        # Switch to the suggestion form
        self.ui.stackedWidget.setCurrentIndex(1)
        
        # Ensure the window is on top and has focus
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.showFullScreen()
        self.activateWindow()
        self.raise_()
    
    def show_problem_list(self):
        """Switch back to the problem list view."""
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def submit_suggestion(self):
        """Submit the suggestion for the current problem."""
        if not self.current_problem:
            return
            
        suggestion_text = self.ui.suggestion_text.toPlainText().strip()
        
        if not suggestion_text:
            QtWidgets.QMessageBox.warning(
                self,
                "Empty Suggestion",
                "Please enter a suggestion before submitting."
            )
            return
            
        # Here you would typically save the suggestion to a database
        # For now, just show a confirmation message
        QtWidgets.QMessageBox.information(
            self,
            "Suggestion Submitted",
            "Thank you! Your suggestion has been submitted."
        )
        
        # Return to the problem list view
        self.show_problem_list()
    
    def submit_suggestions(self):
        """Submit all suggestions and likes."""
        if not self.selected_problems:
            QtWidgets.QMessageBox.warning(
                self,
                "No Selection",
                "Please select at least one problem to prioritize before submitting.",
            )
            return
        
        message = f"You have prioritized {len(self.selected_problems)} problems."
        
        QtWidgets.QMessageBox.information(
            self,
            "Suggestions Submitted",
            message + "\n\nThank you for your input to help improve your community!"
        )
        
        # Go back to the main screen
        self.hide()
        
        if self.parent:
            # If we have a parent, show it
            self.parent.hide()
        else:
            # Standalone mode or no parent provided
            try:
                from main_ui import MyMainScreen
                self.next = MyMainScreen()
                self.next.showFullScreen()
            except ImportError:
                # Just close if we can't navigate
                self.close()
    
    def cancel_clicked(self):
        """Return to the main screen when cancel is clicked."""
        self.hide()
        
        if self.parent:
            # If we have a parent, show it
            self.parent.show()
        else:
            # Standalone mode or no parent provided
            try:
                from main_ui import MyMainScreen
                self.next = MyMainScreen()
                self.next.showFullScreen()
            except ImportError:
                # Just close if we can't navigate
                self.close()


# For standalone testing
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # Sample problem data for testing
    sample_problems = [
        {
            "id": 1,
            "address": "123 Main St, Toronto",
            "problem_type": "Potholes",
            "description": "Large pothole causing traffic issues",
            "date_reported": "2023-03-15"
        },
        {
            "id": 2,
            "address": "456 Queen St, Toronto",
            "problem_type": "Street Light Out",
            "description": "Street light not working at night, safety hazard",
            "date_reported": "2023-03-16"
        }
    ]
    
    # Apply stylesheet if available
    try:
        with open("modern_style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except (FileNotFoundError, IOError):
        pass
    
    suggest_screen = MySuggestScreen(reported_problems=sample_problems)
    suggest_screen.show()
    sys.exit(app.exec_())
