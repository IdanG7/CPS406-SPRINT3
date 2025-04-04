#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Map Dialog Module

This module provides an interactive map interface using OpenStreetMap and PyQt5.
Users can select locations by clicking on the map or searching for addresses
within Toronto.
"""

import sys
import os
import requests
from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QLineEdit, QMessageBox
)
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings
from PyQt5.QtWebChannel import QWebChannel


class MapDialog(QDialog):
    """
    Interactive map dialog using OpenStreetMap.
    
    This dialog allows users to select a location on a map by either clicking
    directly on the map or searching for a location by name. The selected 
    location is converted to a proper address using reverse geocoding.
    
    Attributes:
        addressSelected (pyqtSignal): Signal emitted when an address is selected
    """
    
    # Signal to emit when an address is selected
    addressSelected = pyqtSignal(str)
    
    def __init__(self, parent=None):
        """
        Initialize the map dialog.
        
        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Select Location")
        self.setMinimumSize(900, 700)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)
        
        # Store last clicked coordinates
        self.last_lat = None
        self.last_lng = None
        
        # Setup UI
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface components for the map dialog."""
        main_layout = QVBoxLayout()
        
        # Info label
        info_label = QLabel("Click on the map to select a location or search for an address")
        info_label.setStyleSheet("font-size: 12px; color: #666;")
        main_layout.addWidget(info_label)
        
        # Search bar and buttons at the top
        search_layout = QHBoxLayout()
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search for a location in Toronto")
        self.search_input.setMinimumHeight(40)
        
        self.search_button = QPushButton("Search")
        self.search_button.setMinimumHeight(40)
        self.search_button.clicked.connect(self.search_location)
        
        search_layout.addWidget(self.search_input, 3)
        search_layout.addWidget(self.search_button, 1)
        
        main_layout.addLayout(search_layout)
        
        # Web view for the map
        self.web_view = QWebEngineView()
        self.web_view.page().settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.web_view.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.web_view.page().settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        
        # Create HTML with Leaflet map centered on Toronto
        self.html_content = self._create_map_html()
        self.web_view.setHtml(self.html_content, QUrl("https://leafletjs.com/"))
        self.web_view.loadFinished.connect(self._on_map_loaded)
        
        main_layout.addWidget(self.web_view, 3)
        
        # Selected location display
        location_layout = QHBoxLayout()
        
        self.location_label = QLabel("Selected Location:")
        self.location_display = QLineEdit()
        self.location_display.setReadOnly(True)
        self.location_display.setMinimumHeight(40)
        self.location_display.setPlaceholderText("No location selected")
        
        location_layout.addWidget(self.location_label)
        location_layout.addWidget(self.location_display, 3)
        
        main_layout.addLayout(location_layout)
        
        # Buttons at the bottom
        button_layout = QHBoxLayout()
        
        self.select_button = QPushButton("Use This Location")
        self.select_button.setMinimumHeight(50)
        self.select_button.clicked.connect(self.select_location)
        self.select_button.setEnabled(False)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setMinimumHeight(50)
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.select_button)
        
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)
    
    def _create_map_html(self):
        """
        Create HTML with embedded Leaflet map centered on Toronto.
        
        Returns:
            str: HTML content with the Leaflet map
        """
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Toronto Map</title>
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
            <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
            <style>
                body { margin: 0; padding: 0; }
                #map { position: absolute; top: 0; bottom: 0; width: 100%; height: 100%; }
            </style>
        </head>
        <body>
            <div id="map"></div>
            <script>
                // Initialize the map centered on Toronto
                var map = L.map('map').setView([43.6532, -79.3832], 13);

                // Add OpenStreetMap tiles
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                }).addTo(map);

                // Variable to store the marker
                var marker = null;

                // Function to handle map clicks
                function onMapClick(e) {
                    // Remove existing marker if any
                    if (marker) {
                        map.removeLayer(marker);
                    }
                    
                    // Add a marker at the clicked location
                    marker = L.marker(e.latlng).addTo(map);
                    
                    // Get the coordinates
                    var lat = e.latlng.lat.toFixed(6);
                    var lng = e.latlng.lng.toFixed(6);
                    
                    // Update the document title with coordinates for reverse geocoding
                    document.title = "MAP_COORDS:" + lat + "," + lng;
                }

                // Search function (simplified)
                function searchLocation(query) {
                    // Locations in Toronto
                    var locations = {
                        "downtown": [43.6532, -79.3832],
                        "university": [43.6629, -79.3957],
                        "cn tower": [43.6426, -79.3871],
                        "eaton centre": [43.6544, -79.3807],
                        "kensington": [43.6543, -79.4007],
                        "chinatown": [43.6532, -79.3976],
                        "distillery": [43.6505, -79.3595],
                        "high park": [43.6465, -79.4637],
                        "scarborough": [43.7764, -79.2318],
                        "north york": [43.7615, -79.4111],
                        "etobicoke": [43.6205, -79.5132],
                        "toronto": [43.6532, -79.3832]
                    };
                    
                    // Default to downtown Toronto
                    var targetLocation = [43.6532, -79.3832];
                    var found = false;
                    var lowercaseQuery = query.toLowerCase();
                    
                    // Check if query contains any known location
                    for (var key in locations) {
                        if (lowercaseQuery.includes(key)) {
                            targetLocation = locations[key];
                            found = true;
                            break;
                        }
                    }
                    
                    // Remove existing marker if any
                    if (marker) {
                        map.removeLayer(marker);
                    }
                    
                    // Add a marker at the target location
                    marker = L.marker(targetLocation).addTo(map);
                    
                    // Set view to the location
                    map.setView(targetLocation, found ? 15 : 13);
                    
                    // Update document title with the search query and coordinates
                    if (found) {
                        document.title = "MAP_SEARCH:" + query + "|" + targetLocation[0] + "," + targetLocation[1];
                    } else {
                        document.title = "MAP_SEARCH:" + query + "|" + targetLocation[0] + "," + targetLocation[1];
                    }
                }

                // Add click event listener to the map
                map.on('click', onMapClick);
            </script>
        </body>
        </html>
        """
    
    def _on_map_loaded(self, from_load_map=False):
        """
        Handle map load finished event.
        
        Args:
            from_load_map (bool, optional): Whether this was called from load_map method. Defaults to False.
        """
        # Connect to title changes for communication from JavaScript
        self.web_view.titleChanged.connect(self._on_title_changed)
        
        # Initialize with ready state
        self.web_view.page().runJavaScript("document.title = 'ready';")
    
    def _on_title_changed(self, title):
        """
        Handle title changes from the web page as a communication channel.
        
        Args:
            title (str): The new title of the web page
        """
        if title.startswith("MAP_COORDS:"):
            coords = title[len("MAP_COORDS:"):]
            lat, lng = coords.split(",")
            self.last_lat = float(lat)
            self.last_lng = float(lng)
            
            # Get address from coordinates
            address = self._get_address_from_coords(lat, lng)
            if address:
                self._handle_address_update(address)
            else:
                # Fall back to coordinates if geocoding fails
                self._handle_address_update(f"{lat}, {lng} (Toronto)")
        
        elif title.startswith("MAP_SEARCH:"):
            data = title[len("MAP_SEARCH:"):]
            query, coords = data.split("|")
            lat, lng = coords.split(",")
            self.last_lat = float(lat)
            self.last_lng = float(lng)
            
            # We already have the search term, so use it as the address
            address = f"{query} (Toronto, ON)"
            self._handle_address_update(address)
    
    def _get_address_from_coords(self, lat, lng):
        """
        Convert coordinates to an address using Nominatim API.
        
        Args:
            lat (str): Latitude of the location
            lng (str): Longitude of the location
            
        Returns:
            str or None: Formatted address if successful, None otherwise
        """
        try:
            url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lng}&zoom=18&addressdetails=1"
            headers = {"User-Agent": "CPS406TorontoApp/1.0"}
            response = requests.get(url, headers=headers, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if "address" in data:
                    addr = data["address"]
                    
                    # Format the address nicely based on available components
                    address_parts = []
                    
                    # First try with house number and road
                    if "house_number" in addr and "road" in addr:
                        address_parts.append(f"{addr['house_number']} {addr['road']}")
                    elif "road" in addr:
                        address_parts.append(addr["road"])
                    
                    # Add neighbourhood or suburb if available
                    if "neighbourhood" in addr:
                        address_parts.append(addr["neighbourhood"])
                    elif "suburb" in addr:
                        address_parts.append(addr["suburb"])
                    
                    # Always add city and province
                    if "city" in addr:
                        address_parts.append(addr["city"])
                    else:
                        address_parts.append("Toronto")
                    
                    if "state" in addr:
                        address_parts.append(addr["state"])
                    else:
                        address_parts.append("ON")
                    
                    # Format the final address
                    if address_parts:
                        return ", ".join(address_parts)
                
                # Fall back to display name if we couldn't parse the address
                if "display_name" in data:
                    # Try to truncate to just Toronto information
                    display_name = data["display_name"]
                    toronto_index = display_name.lower().find("toronto")
                    if toronto_index > 0:
                        return display_name[:toronto_index + 7]
                    return display_name
            
            return None
        except Exception as e:
            print(f"Error getting address: {e}")
            return None
    
    def search_location(self):
        """Search for a location on the map based on user input."""
        search_text = self.search_input.text().strip()
        if not search_text:
            return
            
        # Execute JavaScript to search for the location
        js_code = f"searchLocation('{search_text}')"
        self.web_view.page().runJavaScript(js_code)
    
    def _handle_address_update(self, address):
        """
        Update the UI with the selected address.
        
        Args:
            address (str): The selected address
        """
        self.location_display.setText(address)
        self.select_button.setEnabled(True)
    
    def select_location(self):
        """Use the selected location and close the dialog."""
        if self.location_display.text():
            self.addressSelected.emit(self.location_display.text())
            self.accept()

    def load_map(self, address):
        """
        Initialize the map with a specific address location.
        
        Args:
            address (str): The address to display on the map.
        """
        # First render the map
        self._on_map_loaded(True)
        
        # Once the map is loaded, search for the address
        self.search_input.setText(address)
        self.search_location()


# For standalone testing
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MapDialog()
    if dialog.exec_() == QDialog.Accepted:
        print("Selected address:", dialog.location_display.text())
