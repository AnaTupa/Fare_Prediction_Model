import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- PAGE CONFIG ---
st.set_page_config(page_title="Taxi Fare Prediction", layout="wide")

# --- TITLE AND IMAGE ---
# Create three columns and center the image in the middle one
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("taxi.png", use_container_width=True)
st.title("NYC Taxi Fare Prediction App")

# --- LOAD MODEL AND SCALER ---
model = pickle.load(open("fare_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# --- LOAD AND CLEAN ZONE DATA ---
zone_data = pd.read_csv("taxi_zone_lookup.csv")

# Clean and prepare zone data
zone_data = zone_data.dropna(subset=['Zone', 'LocationID', 'Trip Distance (in miles)'])
zone_data['Zone'] = zone_data['Zone'].astype(str)
zone_data['LocationID'] = zone_data['LocationID'].astype(int)
zone_data['Trip Distance (in miles)'] = zone_data['Trip Distance (in miles)'].astype(float)

# Create dictionaries for lookups
zone_dict = {row['Zone']: row['LocationID'] for _, row in zone_data.iterrows()}
distance_dict = {row['Zone']: row['Trip Distance (in miles)'] for _, row in zone_data.iterrows()}
zone_names = sorted(zone_dict.keys())

# --- MAPPINGS ---
ratecode_mapping = {
    1: "1 - Standard rate",
    2: "2 - JFK",
    3: "3 - Newark",
    4: "4 - Nassau or Westchester",
    5: "5 - Negotiated fare",
    6: "6 - Group ride",
    99: "99 - Unknown"
}

payment_mapping = {
    1: "1 - Credit card",
    2: "2 - Cash"
}

hours = [f"{h:02d}:00" for h in range(24)]

days_mapping = {
    0: "0 - Monday",
    1: "1 - Tuesday",
    2: "2 - Wednesday",
    3: "3 - Thursday",
    4: "4 - Friday",
    5: "5 - Saturday",
    6: "6 - Sunday"
}

# --- USER INPUT ---
st.header("Enter Trip Details")

passenger_count = st.selectbox("Passenger Count", options=list(range(1, 10)))

ratecode_display = st.selectbox("Rate Code", options=list(ratecode_mapping.values()))
RatecodeID = int(ratecode_display.split(" - ")[0])

pickup_zone = st.selectbox("Pickup Zone", zone_names)
dropoff_zone = st.selectbox("Dropoff Zone", zone_names)

PULocationID = zone_dict[pickup_zone]
DOLocationID = zone_dict[dropoff_zone]

# Use the average distance between pickup and dropoff
pickup_distance = distance_dict.get(pickup_zone, 1)
dropoff_distance = distance_dict.get(dropoff_zone, 1)
trip_distance = (pickup_distance + dropoff_distance) / 2

payment_display = st.selectbox("Payment Type", options=list(payment_mapping.values()))
payment_type = int(payment_display.split(" - ")[0])

pickup_hour_str = st.selectbox("Pickup Hour", options=hours)
pickup_hour = hours.index(pickup_hour_str)

pickup_day_display = st.selectbox("Pickup Day of Week", options=list(days_mapping.values()))
pickup_dayofweek = int(pickup_day_display.split(" - ")[0])

# User still inputs total trip time
trip_time_minutes = st.number_input("Estimated Total Trip Time (in minutes)", min_value=0.1, format="%.1f")
total_trip_time = trip_time_minutes * 60  # Convert to seconds

# --- TRANSFORM ---
trip_distance_log = np.log(trip_distance)
total_trip_time_log = np.log(total_trip_time)

# --- CREATE INPUT DATA ---
input_data = pd.DataFrame({
    'passenger_count': [passenger_count],
    'RatecodeID': [RatecodeID],
    'PULocationID': [PULocationID],
    'DOLocationID': [DOLocationID],
    'payment_type': [payment_type],
    'pickup_hour': [pickup_hour],
    'pickup_dayofweek': [pickup_dayofweek],
    'trip_distance_log': [trip_distance_log],
    'total_trip_time_log': [total_trip_time_log]
})

# --- SCALE INPUT ---
scaled_input = scaler.transform(input_data)

# --- PREDICT ---
if st.button("Predict Fare"):
    fare_log = model.predict(scaled_input)[0]
    fare = np.exp(fare_log)
    st.success(f"Estimated Fare Amount: ${fare:.2f}")

