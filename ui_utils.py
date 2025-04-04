"""
UI utilities for applying modern styling to the Cypress application.
"""

from PyQt5.QtWidgets import QWidget, QRadioButton, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QPainter
from PyQt5.QtCore import QSize, Qt, QByteArray, QBuffer
from PyQt5.QtSvg import QSvgRenderer
import os
import icons

def apply_stylesheet(app, style_path="modern_style.qss"):
    """Apply the stylesheet to the entire application"""
    try:
        with open(style_path, "r") as f:
            stylesheet = f.read()
            app.setStyleSheet(stylesheet)
    except Exception as e:
        print(f"Error loading stylesheet: {e}")

def create_icon_pixmap(svg_string, width=24, height=24):
    """Convert SVG string to QPixmap"""
    # Convert SVG string to QByteArray
    byte_array = QByteArray(svg_string.strip().encode('utf-8'))
    
    # Create a QPixmap to render on
    pixmap = QPixmap(width, height)
    pixmap.fill(Qt.transparent)
    
    # Render the SVG onto the pixmap
    renderer = QSvgRenderer(byte_array)
    if renderer.isValid():
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
    
    return pixmap

def setup_modern_navigation(parent_widget, use_icons=True):
    """
    Apply modern styling to navigation radio buttons
    """
    # Map radio button names to icon SVGs
    icon_map = {
        "report_button": icons.REPORT_ICON,
        "suggest_button": icons.SUGGEST_ICON,
        "vote_button": icons.VOTE_ICON,
        "rank_button": icons.RANKING_ICON,
        "faq_button": icons.FAQ_ICON,
        "contact_button": icons.CONTACT_ICON,
        "profile_button": icons.PROFILE_ICON,
        "myReports_button": icons.MY_REPORTS_ICON,
        "friend_button": icons.SHARE_ICON,
        "survey_button": icons.SURVEY_ICON,
        "logout_button": icons.LOGOUT_ICON
    }
    
    # Find all radio buttons in the parent widget
    for child in parent_widget.findChildren(QRadioButton):
        if use_icons and child.objectName() in icon_map:
            # Create SVG icon
            pixmap = create_icon_pixmap(icon_map[child.objectName()])
            
            # Get current text
            text = child.text()
            
            # Set icon
            child.setIcon(QIcon(pixmap))
            child.setIconSize(QSize(24, 24))
            
            # Add padding
            child.setText(f"  {text}")
            
            # Set style
            child.setStyleSheet(child.styleSheet() + """
                QRadioButton {
                    padding-left: 5px;
                }
            """)

def apply_card_style(widget, title=""):
    """Apply card-like style to a widget"""
    widget.setStyleSheet("""
        background-color: white;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        padding: 16px;
    """)
    
    if title:
        label = QLabel(title, widget)
        label.setStyleSheet("""
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 18px;
            font-weight: bold;
            color: #2c3e50;
            padding-bottom: 8px;
        """)
        
        # If widget has a layout, add the label to it
        if widget.layout():
            widget.layout().insertWidget(0, label)

def setup_modern_buttons(parent_widget, primary_buttons=None, secondary_buttons=None):
    """Apply modern styling to buttons"""
    if primary_buttons is None:
        primary_buttons = ["go_button", "login_button", "register_button", "submit_button", "report_button"]
    
    if secondary_buttons is None:
        secondary_buttons = ["cancel_button", "delete_button"]
        
    for child in parent_widget.findChildren(QPushButton):
        name = child.objectName()
        
        if name in primary_buttons:
            child.setStyleSheet("""
                background-color: #2979ff;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 14px;
                font-weight: bold;
                min-height: 36px;
            """)
        elif name in secondary_buttons:
            child.setStyleSheet("""
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 14px;
                font-weight: bold;
                min-height: 36px;
            """)

def create_shadow_effect(widget):
    """Create shadow effect for a widget"""
    from PyQt5.QtWidgets import QGraphicsDropShadowEffect
    from PyQt5.QtGui import QColor
    
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(15)
    shadow.setColor(QColor(0, 0, 0, 30))
    shadow.setOffset(0, 2)
    widget.setGraphicsEffect(shadow)
