import streamlit as st
import psutil
import os
import time
import pandas as pd

st.set_page_config(page_title="Server Monitor", layout="wide")

st.title("Server Monitoring")

# Sidebar refresh control
refresh_rate = st.sidebar.slider("⏱ Refresh every (seconds)", 2,5, 60, 10)

# Initialize session state for storing historical metrics
if "metrics" not in st.session_state:
    st.session_state.metrics = pd.DataFrame(columns=["Time", "CPU", "Memory", "Disk", "NetSent"])

# --- Collect Current Metrics ---
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
net_sent = psutil.net_io_counters().bytes_sent / 1024 / 1024  # MB
timestamp = time.strftime("%H:%M:%S")

# Append to session state
new_row = {"Time": timestamp, "CPU": cpu, "Memory": memory, "Disk": disk, "NetSent": net_sent}
st.session_state.metrics = pd.concat(
    [st.session_state.metrics, pd.DataFrame([new_row])],
    ignore_index=True
)

# --- Show Current Metrics ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("CPU Usage (%)", cpu)
with col2:
    st.metric("Memory Usage (%)", f"{memory}%")
with col3:
    st.metric("Disk Usage (%)", f"{disk}%")
with col4:
    st.metric("Network Sent (MB)", f"{net_sent:.2f}")

# --- Charts for Trends ---
st.subheader("📈 Resource Usage Trends")

col1, col2 = st.columns(2)
with col1:
    st.line_chart(st.session_state.metrics.set_index("Time")[["CPU", "Memory"]])
with col2:
    st.line_chart(st.session_state.metrics.set_index("Time")[["Disk", "NetSent"]])

# --- Gunicorn Logs ---
st.subheader("🐍 Gunicorn Logs")
gunicorn_log = "/var/log/gunicorn/error.log"  # or access.log
if os.path.exists(gunicorn_log):
    with open(gunicorn_log) as f:
        st.text("".join(f.readlines()[-8:]))
else:
    st.warning("Gunicorn log file not found.")


# --- Nginx Access Logs ---
st.subheader("🌐 Nginx Access Logs")
nginx_log = "/var/log/nginx/access.log"
if os.path.exists(nginx_log):
    with open(nginx_log) as f:
        st.text("".join(f.readlines()[-15:]))
else:
    st.warning("Nginx access log not found.")

# --- Nginx Error Logs ---
st.subheader("🚨 Nginx Error Logs")
nginx_error = "/var/log/nginx/error.log"
if os.path.exists(nginx_error):
    with open(nginx_error) as f:
        st.text("".join(f.readlines()[-15:]))
else:
    st.warning("Nginx error log not found.")


