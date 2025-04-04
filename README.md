# Cypress - City of Toronto Problem Reporting System

Cypress is a desktop application that allows citizens of Toronto to report problems they observe in the city, suggest solutions to reported problems, and track the status of their reports.

## Features

- **User Authentication**: Register and login to access the system
- **Report Problems**: Submit reports about various issues (potholes, utility failures, etc.)
- **Suggest Solutions**: View reported problems and suggest solutions
- **Track Reports**: View and manage your submitted reports
- **Admin Dashboard**: Administrative interface for managing reports (admin login required)

## Requirements

- Python 3.6 or higher
- PyQt5
- Other dependencies as listed in requirements.txt

## Installation

1. Ensure you have Python installed on your system.
2. Clone or download this repository to your local machine.
3. Install the required dependencies:

```
pip install PyQt5
```

## Running the Application

To start the application, navigate to the project directory and run:

```
python main_ui.py
```

## Usage Guide

1. **Start Screen**: Click "Start" to begin.
2. **Login/Register**: Login with your credentials or register a new account.
   - For testing, you can use:
     - Regular user: Username: `user`, Password: `user123`
     - Admin user: Username: `admin`, Password: `admin123`
3. **Main Menu**: Select an option:
   - Report a Problem: Submit a new problem report
   - Suggest Solutions: View and suggest solutions to existing problems
   - My Reports: View your submitted reports
   - Logout: Return to the login screen

## Project Structure

- `main_ui.py`: Main application entry point
- `LoginScreen.py`: Login interface
- `RegisterScreen.py`: Registration interface
- `MainScreen.py`: Main menu interface
- `ReportScreen.py`: Problem reporting interface
- `MyReports.py`: User reports interface
- `SuggestScreen.py`: Solution suggestion interface
- `SQ_Dialog.py`: Security question dialog
- Other supporting files and resources

## Development

This project was developed using PyQt5 for the GUI components. The application follows a modular design with separate UI classes for each screen.

## Contributors

- CPS406 Software Engineering Team

## License

This project is for educational purposes only.
