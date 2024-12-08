# Django Authentication System 🛡️

A simple Django-based authentication system with functionalities like user login, registration, and password recovery.

## Features ✨

- **User Registration**: Users can register with a username, phone number, and password. Includes validation to ensure unique usernames and phone numbers. Password confirmation is required during registration.
- **User Login**: Users can log in using their username and password. Validates credentials and displays errors for invalid logins.
- **Forgot Password**: Users can recover their credentials by entering their registered phone number. Displays the username and password associated with the phone number if it exists.
- **Homepage and Result Pages**: Simple navigation and placeholder views for home and results.

## Technologies Used 🛠️

- **Backend**: Django (Python)
- **Database**: Django's ORM (default SQLite setup)
- **Frontend**: HTML templates for rendering forms and results

## Setup Instructions ⚙️

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-authentication-system.git
cd django-authentication-system
