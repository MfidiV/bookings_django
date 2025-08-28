# Django Table Booking App

- A Django web application for managing restaurant table reservations.
- Users can register, log in, book tables, edit bookings, delete bookings, and reset passwords.

## Overview

The Django Table Booking App started as a simple CRUD dashboard and gradually evolved into a full booking management system with authentication, booking features, and a password reset flow.

It demonstrates incremental development:

- Start small with CRUD operations.
- Add authentication (register/login/logout).
- Add booking management (create/edit/delete bookings).
- Add a password reset feature with email support.

### Features

- User Registration & Login (email as username)
- Dashboard for personal bookings
- CRUD (Create, Read, Update, Delete) for bookings
- Forgot Password (with token & email via MailHog)
- Secure authentication with Django’s built-in User model

### Tech Stack

- **Backend:** Django (Python 3.x)
- **Database:** SQLite (default, easy for dev)
- **Frontend:** Django Templates + Bootstrap
- **Email Testing:** MailHog (local SMTP testing)
- **Version Control:** Git + GitHub

## Clone the Project

To get a copy of this project locally, run:

```
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


```

