
import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
from collections import deque

# Set page config
st.set_page_config(
    page_title="Water Quality Monitoring",
    page_icon="💧",
    layout="wide"
)

# Initialize session state for historical data
if 'historical_data' not in st.session_state:
    st.session_state.historical_data = deque(maxlen=100)  # Store last 100 readings

def get_sensor_data():
    """
    Simulate sensor readings. Replace this with your actual IoT sensor data collection code.
    """
    return {
        'timestamp': datetime.now(),
        'temperature': np.random.uniform(15, 25),  # °C
        'pH': np.random.uniform(6.5, 8.5),
        'turbidity': np.random.uniform(0, 10),  # NTU
        'flow_rate': np.random.uniform(0, 100),  # L/min
        'dissolved_oxygen': np.random.uniform(6, 12)  # mg/L
    }

def check_threshold(value, param):
    """Check if parameter is within acceptable range"""
    thresholds = {
        'temperature': (15, 25),
        'pH': (6.5, 8.5),
        'turbidity': (0, 10),
        'flow_rate': (10, 90),
        'dissolved_oxygen': (6, 12)
    }
    min_val, max_val = thresholds[param]
    return min_val <= value <= max_val

# Page header
st.title("💧 Water Quality Monitoring Dashboard")
st.markdown("Real-time monitoring of drainage pipe water parameters")

# Create layout
col1, col2, col3 = st.columns(3)
current_data = get_sensor_data()

# Add current reading to historical data
st.session_state.historical_data.append(current_data)

# Display current readings with gauges
with col1:
    st.subheader("Temperature")
    fig_temp = go.Figure(go.Indicator(
        mode="gauge+number",
        value=current_data['temperature'],
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [15, 25]},
               'bar': {'color': "darkblue"},
               'threshold': {
                   'line': {'color': "red", 'width': 4},
                   'thickness': 0.75,
                   'value': 25}}))
    st.plotly_chart(fig_temp)

with col2:
    st.subheader("pH Level")
    fig_ph = go.Figure(go.Indicator(
        mode="gauge+number",
        value=current_data['pH'],
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [0, 14]},
               'bar': {'color': "green"},
               'threshold': {
                   'line': {'color': "red", 'width': 4},
                   'thickness': 0.75,
                   'value': 8.5}}))
    st.plotly_chart(fig_ph)

with col3:
    st.subheader("Dissolved Oxygen")
    fig_do = go.Figure(go.Indicator(
        mode="gauge+number",
        value=current_data['dissolved_oxygen'],
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [0, 15]},
               'bar': {'color': "lightblue"},
               'threshold': {
                   'line': {'color': "red", 'width': 4},
                   'thickness': 0.75,
                   'value': 12}}))
    st.plotly_chart(fig_do)

# Historical data section
st.subheader("Historical Trends")
if st.session_state.historical_data:
    # Convert deque to DataFrame
    df = pd.DataFrame(list(st.session_state.historical_data))
    
    # Create time series plot
    fig = px.line(df, x='timestamp', 
                  y=['temperature', 'pH', 'dissolved_oxygen'],
                  labels={'value': 'Reading', 'timestamp': 'Time'},
                  title='Parameter Trends Over Time')
    st.plotly_chart(fig, use_container_width=True)

    # Display alerts for out-of-range parameters
    st.subheader("Alerts")
    for param in ['temperature', 'pH', 'turbidity', 'flow_rate', 'dissolved_oxygen']:
        if not check_threshold(current_data[param], param):
            st.error(f"⚠️ {param.title()} is out of acceptable range: {current_data[param]:.2f}")

    # Display raw data table
    st.subheader("Raw Data")
    st.dataframe(df.tail(10).style.format({
        'temperature': '{:.2f}',
        'pH': '{:.2f}',
        'turbidity': '{:.2f}',
        'flow_rate': '{:.2f}',
        'dissolved_oxygen': '{:.2f}'
    }))

# Auto-refresh every 5 seconds
time.sleep(5)
st.rerun()
