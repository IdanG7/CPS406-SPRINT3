"""
Helper module that properly loads SVG icons for the application.
"""

from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QByteArray, Qt
from PyQt5.QtSvg import QSvgRenderer
import icons

def svg_to_pixmap(svg_string, width=24, height=24):
    """Convert SVG string to QPixmap for use in the application"""
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

def get_icon(icon_name, width=24, height=24):
    """Get a QPixmap from the icon name"""
    icon_map = {
        "radio_unchecked": icons.RADIO_UNCHECKED,
        "radio_checked": icons.RADIO_CHECKED,
        "dropdown_arrow": icons.DROPDOWN_ARROW,
        "report_icon": icons.REPORT_ICON,
        "suggest_icon": icons.SUGGEST_ICON,
        "vote_icon": icons.VOTE_ICON,
        "ranking_icon": icons.RANKING_ICON,
        "faq_icon": icons.FAQ_ICON,
        "contact_icon": icons.CONTACT_ICON,
        "profile_icon": icons.PROFILE_ICON, 
        "my_reports_icon": icons.MY_REPORTS_ICON,
        "share_icon": icons.SHARE_ICON,
        "survey_icon": icons.SURVEY_ICON,
        "logout_icon": icons.LOGOUT_ICON
    }
    
    if icon_name not in icon_map:
        return QPixmap()
    
    return svg_to_pixmap(icon_map[icon_name], width, height)
