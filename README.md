# **Cypress - City of Toronto Street Issue Reporting System**

A PyQt5-based desktop application designed to help citizens report and manage street-related problems in Toronto. Administrators can view, respond to, and resolve submitted reports. Built for CPS406, this project reflects agile software development principles including sprint-based planning, testing, and delivery.

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white)

---

## 📑 Table of Contents
- [🚀 Features](#-features)
- [🛠️ Getting Started](#️-getting-started)
- [⚙️ Installation](#%EF%B8%8F-installation)
- [📦 Sprint 3 Summary](#-sprint-3-summary)
- [📋 Product Backlog](#-product-backlog)
- [✅ Test Matrix](#-test-matrix)
- [📊 Velocity Graph](#-velocity-graph)
- [🧑‍💻 Contributors](#-contributors)

---

## 🚀 Features

- 📍 Interactive map-based reporting
- 🛠️ Report problems with categorized types and attachments
- 🧾 "My Reports" dashboard for tracking, editing, deleting
- 💬 Suggest solutions and vote on ideas
- 🔐 User registration with security question validation
- ⚙️ Admin dashboard to manage users and statuses
- 🎨 Unified modern UI using `ui_utils.py`
- 💾 System-wide settings for backups, theming, and preferences

---

## 🛠️ Getting Started

Follow the instructions below to run the Cypress system on your local machine using **Visual Studio Code**.


### 📚 Prerequisites

Make sure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [VS Code](https://code.visualstudio.com/)
- [Git (optional)](https://git-scm.com/)



## ⚙️ Installation

### 🔧 Step 1: Clone or extract the project

```bash
1) git clone https://github.com/yourusername/cypress-app.git
2) cd cypress-app
3) pip install -r requirements.txt
4) Run in terminal: python main_ui.py
```
---
## 🔒 Logins
- User Login: user, user123
- Admin Login: admin, admin123
---
## 📦 Sprint 3 Summary

- ✅ Finalized and polished all core features from Sprint 2
- ✅ Built `SuggestScreen`, `MyReports`, `SystemSettings`, `UserManagementScreen`
- ✅ Applied consistent modern styling across all modules
- ✅ Connected security question system for enhanced registration
- ✅ Created and executed full test suite
- ✅ Delivered ZIP archive and demo video walkthrough

---


## 📋 Product Backlog

| User Story | Status | Priority | Est. Effort | Actual Effort | Sprint Completed |
|------------|--------|----------|-------------|----------------|------------------|
| As a citizen, I want to click on a map to report a street-related problem. | ✅ Launched | 🔴 High | 5 | 6 | March 4 |
| As a citizen, I want to select the type of problem (e.g., pothole, broken light). | ✅ Launched | 🔴 High | 2 | 2 | March 4 |
| As a citizen, I want to attach a description and images to my report. | ✅ Launched | 🟠 Medium | 4 | 2 | March 11 |
| As a citizen, I want to receive a confirmation message after submitting my report. | ✅ Launched | 🟢 Low | 1 | 2 | March 18 |
| As a citizen, I want to receive status updates on my reported problems. | ✅ Launched | 🔴 High | 3 | 2 | March 4 |
| As a citizen, I want to subscribe to updates for reported problems. | ✅ Launched | 🟢 Low | 3 | 1 | March 25 |
| As a citizen, I want to view past reported problems. | ✅ Launched | 🟠 Medium | 2 | 4 | March 25 |
| As an admin, I want to view all reported problems in an organized list. | ✅ Launched | 🔴 High | 3 | 1 | March 4 |
| As an admin, I want to update the status of a reported problem. | ✅ Launched | 🔴 High | 4 | 3 | March 11 |
| As an admin, I want to approve or reject reports. | ✅ Launched | 🟠 Medium | 3 | 4 | March 11 |
| As an admin, I want to resolve a reported issue by providing a resolution statement. | ✅ Launched | 🟠 Medium | 3 | 3 | April 4 |
| As an admin, I want to record changes in real-time. | ✅ Launched | 🟢 Low | 2 | 2 | April 4 |
| As a system user, I want to prevent false reports by implementing bot detection and user flags. | ✅ Launched | 🔴 High | 4 | 4 | April 4 |
| As a system user, I want to identify duplicate reports. | ✅ Launched | 🟠 Medium | 3 | 4 | April 4 |
| As an admin, I want to review flagged reports. | ✅ Launched | 🟢 Low | 2 | 2 | April 4 |
| As an admin, I want to track which reports have pending actions. | ✅ Launched | 🟠 Medium | 2 | 3 | April 4 |
| As a user, I want to log into my account so I can access and interact with the Cypress platform. | ✅ Launched | 🔴 High | 3 | 3 | March 4 |
| As a user, I want to be notified when my login attempt fails so I can correct my credentials. | ✅ Launched | 🔴 High | 2 | 2 | March 4 |

---

## ✅ Test Matrix

| Test ID | Test Condition | Test Input | Expected Output |
|---------|----------------|------------|------------------|
| TC01 | Submit a new pothole report | Click on map, select "Pothole", add photo + description | Report saved in database, confirmation shown |
| TC02 | Detect duplicate reports | Submit same location + issue type | Duplicate warning displayed |
| TC03 | Display confirmation after submission | Complete report form, click "Submit" | Modal or toast notification appears |
| TC04 | Track report status | Open "My Reports", select existing report | Status + update history shown |
| TC05 | Subscribe to a report's updates | Click "Subscribe", enter email/phone | Success message shown; updates enabled |
| TC06 | Admin updates report status | Change to “In Progress” or “Resolved” | Status updated in DB, subscriber notified |
| TC07 | Prevent false/bot reports | Submit spam/auto-filled form | CAPTCHA shown or error triggered |
| TC08 | Admin reviews flagged reports | Access “Flagged Reports”, approve one | Report updated to Approved, flag removed |
| TC09 | View reports on the map | Click “View Reports” from menu | Map loads with pins for each report |
| TC10 | Attach image and description | Upload image, add description | Media/text saved, shown in admin panel |
| TC11 | Valid Login | Correct email + password | Login successful, redirected to dashboard |
| TC12 | Invalid Login | Incorrect email/password | Error: "Invalid email or password." |

---

## 📊 Velocity Graph

> 📈 Our team’s velocity graph is included in the Sprint 3 documentation PDF. It compares estimated and actual effort for each user story and illustrates how our prediction accuracy improved from Sprint 2.

---

## 🧑‍💻 Contributors

| Name              | Student ID     |
|-------------------|----------------|
| Idan Gurevich     | 501230092      |
| Roman Abramovich  | 501232016      |
| Anthony Garcia    | 501238522      |
