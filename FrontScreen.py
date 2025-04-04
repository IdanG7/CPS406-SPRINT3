from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrontScreen(object):
    def setupUi(self, FrontScreen):
        FrontScreen.setObjectName("FrontScreen")
        FrontScreen.setWindowIcon(QtGui.QIcon('images/cypress_logo.png'))
        FrontScreen.setFixedSize(900, 700)  
        FrontScreen.setWindowTitle("Cypress")
        FrontScreen.setWindowOpacity(1.0)
        FrontScreen.setAutoFillBackground(False)
        
        FrontScreen.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                      stop:0 #f5f7fa, stop:1 #c3cfe2);
            }
            QLabel {
                color: #2c3e50;
            }
            QStatusBar {
                background-color: #34495e;
                color: white;
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(FrontScreen)
        self.centralwidget.setObjectName("centralwidget")
        
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(40, 40, 40, 40)
        self.mainLayout.setSpacing(30)
        self.mainLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.setObjectName("mainLayout")
        
        self.headerContainer = QtWidgets.QWidget(self.centralwidget)
        self.headerContainer.setObjectName("headerContainer")
        self.headerContainer.setStyleSheet("""
            QWidget#headerContainer {
                background-color: rgba(255, 255, 255, 180);
                border-radius: 10px;
                padding: 10px;
            }
        """)
        
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QtGui.QColor(0, 0, 0, 80))
        shadow.setOffset(0, 2)
        self.headerContainer.setGraphicsEffect(shadow)
        
        self.headerLayout = QtWidgets.QVBoxLayout(self.headerContainer)
        self.headerLayout.setContentsMargins(20, 20, 20, 20)
        self.headerLayout.setAlignment(QtCore.Qt.AlignCenter)
        
        self.Header = QtWidgets.QLabel(self.headerContainer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)  
        font.setBold(True)
        self.Header.setFont(font)
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setStyleSheet("color: #2c3e50;")
        self.Header.setObjectName("Header")
        self.headerLayout.addWidget(self.Header)
        
        self.tagline = QtWidgets.QLabel(self.headerContainer)
        tagline_font = QtGui.QFont()
        tagline_font.setPointSize(16)
        tagline_font.setItalic(True)
        self.tagline.setFont(tagline_font)
        self.tagline.setAlignment(QtCore.Qt.AlignCenter)
        self.tagline.setStyleSheet("color: #7f8c8d; margin-top: -10px;")
        self.tagline.setObjectName("tagline")
        self.headerLayout.addWidget(self.tagline)
        
        self.mainLayout.addWidget(self.headerContainer)
        
        self.logoContainer = QtWidgets.QWidget(self.centralwidget)
        self.logoContainer.setObjectName("logoContainer")
        self.logoContainer.setStyleSheet("""
            QWidget#logoContainer {
                background-color: rgba(255, 255, 255, 180);
                border-radius: 10px;
                padding: 10px;
            }
        """)
        
        logo_shadow = QtWidgets.QGraphicsDropShadowEffect()
        logo_shadow.setBlurRadius(15)
        logo_shadow.setColor(QtGui.QColor(0, 0, 0, 80))
        logo_shadow.setOffset(0, 2)
        self.logoContainer.setGraphicsEffect(logo_shadow)
        
        self.logoLayout = QtWidgets.QVBoxLayout(self.logoContainer)
        self.logoLayout.setContentsMargins(20, 20, 20, 20)
        self.logoLayout.setAlignment(QtCore.Qt.AlignCenter)
        
        self.toronto_logo_label = QtWidgets.QLabel(self.logoContainer)
        self.toronto_logo_label.setMinimumSize(QtCore.QSize(200, 140))
        self.toronto_logo_label.setMaximumSize(QtCore.QSize(200, 140))
        self.toronto_logo_label.setText("")
        self.toronto_logo_label.setPixmap(QtGui.QPixmap("images/toronto_logo.jpg"))
        self.toronto_logo_label.setScaledContents(True)
        self.toronto_logo_label.setObjectName("toronto_logo_label")
        
        self.toronto_logo_label.setStyleSheet("""
            border: 2px solid #3498db;
            border-radius: 5px;
        """)
        
        self.logoLayout.addWidget(self.toronto_logo_label)
        
        self.main_screen_text = QtWidgets.QLabel(self.logoContainer)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.main_screen_text.setFont(font)
        self.main_screen_text.setAlignment(QtCore.Qt.AlignCenter)
        self.main_screen_text.setStyleSheet("color: #2c3e50; margin-top: 10px;")
        self.main_screen_text.setObjectName("main_screen_text")
        self.logoLayout.addWidget(self.main_screen_text)
        
        self.mainLayout.addWidget(self.logoContainer)
        
        self.infoContainer = QtWidgets.QWidget(self.centralwidget)
        self.infoContainer.setObjectName("infoContainer")
        self.infoContainer.setStyleSheet("""
            QWidget#infoContainer {
                background-color: rgba(255, 255, 255, 180);
                border-radius: 10px;
                padding: 15px;
            }
        """)
        
        info_shadow = QtWidgets.QGraphicsDropShadowEffect()
        info_shadow.setBlurRadius(15)
        info_shadow.setColor(QtGui.QColor(0, 0, 0, 80))
        info_shadow.setOffset(0, 2)
        self.infoContainer.setGraphicsEffect(info_shadow)
        
        self.infoLayout = QtWidgets.QVBoxLayout(self.infoContainer)
        self.infoLayout.setContentsMargins(20, 20, 20, 20)
        
        self.app_description = QtWidgets.QLabel(self.infoContainer)
        description_font = QtGui.QFont()
        description_font.setPointSize(12)
        self.app_description.setFont(description_font)
        self.app_description.setAlignment(QtCore.Qt.AlignCenter)
        self.app_description.setWordWrap(True)
        self.app_description.setStyleSheet("color: #34495e; line-height: 1.5;")
        self.app_description.setObjectName("app_description")
        self.infoLayout.addWidget(self.app_description)
        
        self.features_title = QtWidgets.QLabel(self.infoContainer)
        features_title_font = QtGui.QFont()
        features_title_font.setPointSize(12)
        features_title_font.setBold(True)
        self.features_title.setFont(features_title_font)
        self.features_title.setAlignment(QtCore.Qt.AlignCenter)
        self.features_title.setStyleSheet("color: #2980b9; margin-top: 10px;")
        self.features_title.setObjectName("features_title")
        self.infoLayout.addWidget(self.features_title)
        
        self.features_list = QtWidgets.QWidget(self.infoContainer)
        self.features_layout = QtWidgets.QHBoxLayout(self.features_list)
        self.features_layout.setContentsMargins(0, 10, 0, 10)
        
        self.features_left = QtWidgets.QLabel(self.features_list)
        self.features_left.setFont(description_font)
        self.features_left.setStyleSheet("color: #34495e;")
        self.features_left.setAlignment(QtCore.Qt.AlignLeft)
        self.features_layout.addWidget(self.features_left)
        
        self.features_right = QtWidgets.QLabel(self.features_list)
        self.features_right.setFont(description_font)
        self.features_right.setStyleSheet("color: #34495e;")
        self.features_right.setAlignment(QtCore.Qt.AlignLeft)
        self.features_layout.addWidget(self.features_right)
        
        self.infoLayout.addWidget(self.features_list)
        
        self.mainLayout.addWidget(self.infoContainer)
        
        self.buttonContainer = QtWidgets.QWidget(self.centralwidget)
        self.buttonContainer.setObjectName("buttonContainer")
        self.buttonContainer.setStyleSheet("""
            QWidget#buttonContainer {
                background-color: rgba(255, 255, 255, 180);
                border-radius: 10px;
                padding: 15px;
            }
        """)
        
        button_shadow = QtWidgets.QGraphicsDropShadowEffect()
        button_shadow.setBlurRadius(15)
        button_shadow.setColor(QtGui.QColor(0, 0, 0, 80))
        button_shadow.setOffset(0, 2)
        self.buttonContainer.setGraphicsEffect(button_shadow)
        
        self.buttonLayout = QtWidgets.QVBoxLayout(self.buttonContainer)
        self.buttonLayout.setContentsMargins(20, 20, 20, 20)
        self.buttonLayout.setSpacing(15)
        self.buttonLayout.setAlignment(QtCore.Qt.AlignCenter)
        
        self.english_button = QtWidgets.QPushButton(self.buttonContainer)
        self.english_button.setMinimumSize(QtCore.QSize(400, 80))
        self.english_button.setMaximumSize(QtCore.QSize(400, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.english_button.setFont(font)
        self.english_button.setObjectName("english_button")
        self.english_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f6dad;
            }
        """)
        
        button_effect = QtWidgets.QGraphicsDropShadowEffect()
        button_effect.setBlurRadius(15)
        button_effect.setColor(QtGui.QColor(0, 0, 0, 80))
        button_effect.setOffset(0, 2)
        self.english_button.setGraphicsEffect(button_effect)
        
        self.buttonLayout.addWidget(self.english_button, 0, QtCore.Qt.AlignCenter)
        
        self.version_info = QtWidgets.QLabel(self.buttonContainer)
        version_font = QtGui.QFont()
        version_font.setPointSize(9)
        self.version_info.setFont(version_font)
        self.version_info.setAlignment(QtCore.Qt.AlignCenter)
        self.version_info.setStyleSheet("color: #7f8c8d; margin-top: 5px;")
        self.version_info.setObjectName("version_info")
        self.buttonLayout.addWidget(self.version_info)
        
        self.mainLayout.addWidget(self.buttonContainer)
        
        FrontScreen.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(FrontScreen)
        self.statusbar.setObjectName("statusbar")
        FrontScreen.setStatusBar(self.statusbar)

        self.nameUi(FrontScreen)
        QtCore.QMetaObject.connectSlotsByName(FrontScreen)

    def nameUi(self, FrontScreen):
        FrontScreen.setWindowTitle("Cypress")
        self.Header.setText("CYPRESS")
        self.tagline.setText("Keeping Our City Streets Clean and Safe")
        self.english_button.setText("START")
        self.main_screen_text.setText("City of Toronto")
        self.app_description.setText(
            "Welcome to Cypress, the official City of Toronto application for reporting "
            "and tracking street-related issues. Help us maintain our beautiful city by "
            "reporting problems you encounter around Toronto.")
        self.features_title.setText("Key Features:")
        self.features_left.setText(
            "• Report street problems\n"
            "• Track your submitted reports\n"
            "• View report status updates")
        self.features_right.setText(
            "• Suggest improvements\n"
            "• View problem locations on map\n"
            "• Receive notifications")
        self.version_info.setText("Version 2.0 2025 City of Toronto")
        self.statusbar.showMessage("Ready to serve Toronto citizens")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrontScreen = QtWidgets.QMainWindow()
    ui = Ui_FrontScreen()
    ui.setupUi(FrontScreen)
    FrontScreen.show()
    sys.exit(app.exec_())
