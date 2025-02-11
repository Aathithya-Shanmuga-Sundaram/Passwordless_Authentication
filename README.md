# Passwordless Authentication System

## Overview
This project is a **Flask-based passwordless authentication system** that identifies users using **device fingerprinting** instead of passwords. It collects the user's **User Agent, IP Address, Timezone, and Screen Resolution** to authenticate them. If any of these details do not match the stored data, authentication fails.

## Features
- **Passwordless Login:** Uses device fingerprinting instead of traditional passwords.
- **User Identification Factors:**
  - User Agent
  - IP Address
  - Timezone (set via JavaScript)
  - Screen Resolution (set via JavaScript)
- **Registration System:** Stores user details for future authentication.
- **Login Authentication:** Compares stored and current user details for verification.
- **Flask Backend:** Lightweight and easy-to-deploy application.

## Tech Stack
- **Frontend:** HTML, JavaScript (for collecting timezone and screen resolution)
- **Backend:** Python (Flask framework)
- **Hosting:** GitHub Repository (Frontend can be hosted via GitHub Pages, backend requires deployment)
- **Storage:** In-memory dictionary (can be upgraded to a database)

## How It Works
1. **User Registration:**
   - User enters their username and email.
   - The system captures their **User Agent, IP Address, Timezone, and Screen Resolution**.
   - These details are stored for future authentication.

2. **User Login:**
   - User enters their username.
   - The system retrieves the current **User Agent, IP Address, Timezone, and Screen Resolution**.
   - It compares them with the stored values.
   - If all details match, login is successful.
   - If any detail differs, authentication fails.

## Installation & Setup
### Prerequisites
- Python 3.x installed
- Flask installed (`pip install flask`)

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Aathithya-Shanmuga-Sundaram/Passwordless_Authentication.git
   cd Passwordless_Authentication
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open a web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
5. Register a user and test the authentication system.

## Deployment
- Use **Heroku, Render, or any Flask-compatible cloud platform** to host the backend.
- Frontend can be hosted using **GitHub Pages**.

## Future Enhancements
- **Database Integration:** Store authentication data in a database.
- **Multi-Factor Authentication (MFA):** Add additional security layers.
- **OAuth Integration:** Support third-party authentication providers.
- **Enhanced Fingerprinting:** Include more device-based identifiers.

## Contributing
Contributions are welcome! Feel free to submit **issues** and **pull requests**.
