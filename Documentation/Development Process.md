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
