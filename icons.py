"""
This module provides base64-encoded SVG icons for the application.
By using base64-encoded SVGs, we can embed the icons directly in the code
without requiring external files.
"""

# Radio button icons
RADIO_UNCHECKED = """
<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
  <circle cx="9" cy="9" r="8" fill="none" stroke="#757575" stroke-width="1.5"/>
</svg>
"""

RADIO_CHECKED = """
<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
  <circle cx="9" cy="9" r="8" fill="none" stroke="#2979ff" stroke-width="1.5"/>
  <circle cx="9" cy="9" r="5" fill="#2979ff"/>
</svg>
"""

# Dropdown arrow
DROPDOWN_ARROW = """
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="#757575" d="M8 11L3 6h10z"/>
</svg>
"""

# Report icon
REPORT_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path fill="#2979ff" d="M14,2H6C4.9,2,4,2.9,4,4v16c0,1.1,0.9,2,2,2h12c1.1,0,2-0.9,2-2V8L14,2z M16,16H8v-2h8V16z M16,12H8v-2h8V12z M13,9V3.5L18.5,9H13z"/>
</svg>
"""

# Suggestion icon
SUGGEST_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path fill="#2979ff" d="M9,21c0,0.5,0.4,1,1,1h4c0.6,0,1-0.5,1-1v-1H9V21z M12,2C8.1,2,5,5.1,5,9c0,2.4,1.2,4.5,3,5.7V17c0,0.5,0.4,1,1,1h6c0.6,0,1-0.5,1-1v-2.3c1.8-1.3,3-3.4,3-5.7C19,5.1,15.9,2,12,2z M13.3,13.7L13,14v2h-2v-2l-0.3-0.3C9.4,12.8,9,11.4,9,10.5V9.9l0.9-0.7C10.3,8.8,11.1,8.5,12,8.5s1.7,0.3,2.1,0.7L15,9.9v0.6C15,11.4,14.6,12.8,13.3,13.7z"/>
</svg>
"""

# Vote icon
VOTE_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path fill="#2979ff" d="M18,13h-5v5h-2v-5H6v-2h5V6h2v5h5V13z"/>
</svg>
"""

# Ranking icon
RANKING_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path fill="#2979ff" d="M7,21h2v-2H7V21z M11,21h2v-4h-2V21z M7,17h2v-4H7V17z M15,21h2v-6h-2V21z M3,11h2V3H3V11z M11,13h2v-4h-2V13z M15,13h2V3h-2V13z M3,15h2v-2H3V15z M7,13h2V3H7V13z"/>
</svg>
"""

# FAQ icon
FAQ_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path fill="#2979ff" d="M12,2C6.48,2,2,6.48,2,12s4.48,10,10,10s10-4.48,10-10S17.52,2,12,2z M13,19h-2v-2h2V19z M15.07,11.25l-0.9,0.92C13.45,12.9,13,13.5,13,15h-2v-0.5c0-1.1,0.45-2.1,1.17-2.83l1.24-1.26c0.37-0.36,0.59-0.86,0.59-1.41c0-1.1-0.9-2-2-2s-2,0.9-2,2H8c0-2.21,1.79-4,4-4s4,1.79,4,4C16,9.67,15.64,10.59,15.07,11.25z"/>
</svg>
"""

# Contact icon
CONTACT_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path fill="#2979ff" d="M20,4H4C2.9,4,2,4.9,2,6v12c0,1.1,0.9,2,2,2h16c1.1,0,2-0.9,2-2V6C22,4.9,21.1,4,20,4z M20,8l-8,5L4,8V6l8,5l8-5V8z"/>
</svg>
"""

# Profile icon
PROFILE_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path fill="#2979ff" d="M12,2C6.48,2,2,6.48,2,12s4.48,10,10,10s10-4.48,10-10S17.52,2,12,2z M12,5c1.66,0,3,1.34,3,3s-1.34,3-3,3s-3-1.34-3-3S10.34,5,12,5z M12,19.2c-2.5,0-4.71-1.28-6-3.22c0.03-1.99,4-3.08,6-3.08c1.99,0,5.97,1.09,6,3.08C16.71,17.92,14.5,19.2,12,19.2z"/>
</svg>
"""

# My reports icon
MY_REPORTS_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path fill="#2979ff" d="M19,3H5C3.9,3,3,3.9,3,5v14c0,1.1,0.9,2,2,2h14c1.1,0,2-0.9,2-2V5C21,3.9,20.1,3,19,3z M14,17H7v-2h7V17z M17,13H7v-2h10V13z M17,9H7V7h10V9z"/>
</svg>
"""

# Share icon
SHARE_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path fill="#2979ff" d="M18,16.08c-0.76,0-1.44,0.3-1.96,0.77L8.91,12.7C8.96,12.47,9,12.24,9,12s-0.04-0.47-0.09-0.7l7.05-4.11C16.5,7.69,17.21,8,18,8c1.66,0,3-1.34,3-3s-1.34-3-3-3s-3,1.34-3,3c0,0.24,0.04,0.47,0.09,0.7L8.04,9.81C7.5,9.31,6.79,9,6,9c-1.66,0-3,1.34-3,3s1.34,3,3,3c0.79,0,1.5-0.31,2.04-0.81l7.12,4.16c-0.05,0.21-0.08,0.43-0.08,0.65c0,1.61,1.31,2.92,2.92,2.92s2.92-1.31,2.92-2.92C20.92,17.39,19.61,16.08,18,16.08z"/>
</svg>
"""

# Survey icon
SURVEY_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path fill="#2979ff" d="M18,9l-1.41-1.42L10,14.17l-2.59-2.58L6,13l4,4L18,9z M19,3h-1V1h-2v2H8V1H6v2H5C3.89,3,3.01,3.9,3.01,5L3,19c0,1.1,0.89,2,2,2h14c1.1,0,2-0.9,2-2V5C21,3.9,20.1,3,19,3z M19,19H5V8h14V19z"/>
</svg>
"""

# Logout icon
LOGOUT_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path fill="#f44336" d="M10.09,15.59L11.5,17l5-5l-5-5l-1.41,1.41L12.67,11H3v2h9.67L10.09,15.59z M19,3H5C3.89,3,3,3.9,3,5v4h2V5h14v14H5v-4H3v4c0,1.1,0.89,2,2,2h14c1.1,0,2-0.9,2-2V5C21,3.9,20.1,3,19,3z"/>
</svg>
"""

def svg_to_qt(svg_string, width=24, height=24):
    """
    Convert SVG string to base64 encoded data URL for PyQt
    """
    import base64
    encoded = base64.b64encode(svg_string.strip().encode('utf-8')).decode('ascii')
    return f"data:image/svg+xml;base64,{encoded}"
