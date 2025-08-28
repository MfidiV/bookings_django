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

## Development Process

### Phase 1: CRUD Dashboard

#### Booking Model
- Created a `Booking` model linked to Django’s `User` model.
- Fields included:
  - `user` (ForeignKey to User)
  - `name` (CharField)
  - `table_number` (PositiveIntegerField)
  - `date` (DateField)
  - `time` (TimeField)

#### CRUD Views
- Implemented views for:
  - Add Booking
  - Edit Booking
  - Delete Booking

#### Dashboard
- Built a dashboard displaying all bookings for the logged-in user.
- Used `Booking.objects.filter(user=request.user)` to ensure user-specific bookings.

### Phase 2: Authentication

#### Registration
- Created a custom `RegisterForm` with fields:
  - First name
  - Email
  - Password
  - Confirm password
- Validation checks:
  - Unique email
  - Password confirmation

#### Login & Logout
- Used `authenticate()` and `login()` for user login.
- Used `logout()` to end user sessions.

### Phase 3: User-specific Bookings

- Each booking linked to the logged-in user.
- Users can only manage their own bookings.
- Routes:
  - `add_booking/`
  - `edit_booking/<id>/`
  - `delete_booking/<id>/`
- Ownership validation implemented to prevent unauthorized edits/deletes.

### Phase 4: Forgot Password Workflow

#### ForgotPasswordForm
- Form for users to submit their email to reset password.

#### Token Generation
- Used Python `secrets` module to generate a secure token.
- Token stored temporarily to identify user.

#### Reset Password Email
- Email sent with a reset link containing the token.
- Used MailHog for local testing.

#### Reset Password View
- Verifies token validity.
- Allows secure password reset.
