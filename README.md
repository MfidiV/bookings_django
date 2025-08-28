# Django Table Booking App

A Django web application for managing restaurant table reservations.  
Users can register, log in, book tables, edit bookings, delete bookings, and reset passwords.

## Overview

The Django Table Booking App started as a simple CRUD dashboard and gradually evolved into a full booking management system with authentication, booking features, and a password reset flow.

It demonstrates incremental development:

- Start small with CRUD operations.
- Add authentication (register/login/logout).
- Add booking management (create/edit/delete bookings).
- Add a password reset feature with email support.

## Features

- User Registration & Login (email as username)
- Dashboard for personal bookings
- CRUD (Create, Read, Update, Delete) for bookings
- Forgot Password (with token & email via MailHog)
- Secure authentication with Django’s built-in User model

## Tech Stack

- **Backend:** Django (Python 3.x)
- **Database:** SQLite (default, easy for development)
- **Frontend:** Django Templates + Bootstrap
- **Email Testing:** MailHog (local SMTP testing)
- **Version Control:** Git + GitHub

## Clone & Setup the Project

Run the following commands in your terminal to set up the project:

```bash
# Clone the repository
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>

# Create and activate a virtual environment
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create a superuser (optional, for admin access)
python manage.py createsuperuser

# Run the development server
python manage.py runserver

# Open the app in your browser at
# http://127.0.0.1:8000/
```

**Usage**

- Register a new account or log in with an existing user.

- Navigate to the dashboard to view, add, edit, or delete bookings.

- Use the forgot password feature to reset your password if needed.

- Admin users can access the Django admin panel at /admin/.

**Email Testing**

For local email testing (password resets), use MailHog
see maillog documentation

**Contributing**

1.Fork the repository.

2.Create a new branch (git checkout -b feature/your-feature).

3.Commit your changes (git commit -m 'Add some feature').

4.Push to the branch (git push origin feature/your-feature).

5.Open a pull request.

