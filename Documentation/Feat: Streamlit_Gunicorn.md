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


## For streamlit server monitoring app

## Features
- **System Metrics Monitoring**  
  - CPU, Memory, Disk, and Network usage  
- **Trend Visualization**  
  - Line charts for historical data  
- **Log Monitoring**  
  - Gunicorn error logs  
  - Nginx access & error logs  
- **Custom Refresh Interval**  
  - Adjustable via sidebar  

## Development Workflow
1. **Environment Setup**
   - Create virtual environment
   - Install dependencies (`streamlit`, `psutil`, `pandas`)

2. **Core Functionality**
   - Used `psutil` to fetch CPU, memory, disk, and network stats
   - Plotted results using Streamlit charts

3. **Logging Integration**
   - Used `os` to interact with log files:
     - Gunicorn error log
     - Nginx access log
     - Nginx error log  

4. **Testing**
   - Ran the app locally with `streamlit run app.py`
   - Stress tested CPU, memory, and network

---
