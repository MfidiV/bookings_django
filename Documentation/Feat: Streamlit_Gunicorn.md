## Development Process: Gunicorn & Streamlit Integration


**Overview**

This document outlines the development process of deploying the Django Table Booking App with Gunicorn for production and integrating Streamlit for real-time monitoring of resources and logs.

**Phase 1: Gunicorn setup**
- Make sure your workin on your venv:
1. Install Gunicorn
```
pip install gunicorn
```
2. Verify Django wsgi.py

Ensure your Django app has a wsgi.py file in the project directory (usually <project_name>/wsgi.py):

<img width="694" height="109" alt="image" src="https://github.com/user-attachments/assets/85b5d7be-7775-4b58-ac60-0290efc8a64d" />

3. Run with Gunicorn

From the root of your project:

```
gunicorn bookings.wsgi:application --bind 0.0.0.0:8000
```

4. You may create a systemd Service (Optional for Linux Deployment)
Create a gunicorn.service file:
