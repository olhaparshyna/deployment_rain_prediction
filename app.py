import streamlit as st
import pandas as pd
import numpy as np
import joblib

def predict_rain(input_dict):
    model = joblib.load('models/aussie_rain_pipeline.joblib')
    
    input_df = pd.DataFrame([input_dict])
    
    input_df['Date'] = pd.to_datetime(input_df['Date'])

    prediction = model.predict(input_df)
    return prediction[0]

st.title('Прогноз дощу в Австралії')
st.markdown('Введіть метеорологічні параметри, щоб передбачити, чи буде дощ завтра.')

st.header("Введіть дані спостереження:")

date = st.date_input("Date", value=pd.to_datetime("2021-06-19"))

# Категоріальні поля
location = st.selectbox("Location", ['Katherine', 'Sydney', 'Melbourne', 'Darwin']) 
wind_gust_dir = st.selectbox("WindGustDir", ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
wind_dir_9am = st.selectbox("WindDir9am", ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
wind_dir_3pm = st.selectbox("WindDir3pm", ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
rain_today = st.selectbox("RainToday", ['Yes', 'No'])

# Числові поля
min_temp = st.number_input("MinTemp (°C)", value=23.2)
max_temp = st.number_input("MaxTemp (°C)", value=33.2)
rainfall = st.number_input("Rainfall (mm)", value=10.2)
evaporation = st.number_input("Evaporation (mm)", value=4.2)
sunshine = st.number_input("Sunshine", min_value=0.0, max_value=24.0, value=0.0, step=0.1)
wind_gust_speed = st.number_input("WindGustSpeed", value=52.0)
wind_speed_9am = st.number_input("WindSpeed9am", value=13.0)
wind_speed_3pm = st.number_input("WindSpeed3pm", value=20.0)
humidity_9am = st.number_input("Humidity9am", value=89.0)
humidity_3pm = st.number_input("Humidity3pm", value=58.0)
pressure_9am = st.number_input("Pressure9am", value=1004.8)
pressure_3pm = st.number_input("Pressure3pm", value=1001.5)
cloud_9am = st.number_input("Cloud9am", value=8.0)
cloud_3pm = st.number_input("Cloud3pm", value=5.0)
temp_9am = st.number_input("Temp9am", value=25.7)
temp_3pm = st.number_input("Temp3pm", value=33.0)

if st.button("Прогнозувати, чи буде дощ завтра"):
    new_input = {
        'Date': date,
        'Location': location,
        'MinTemp': min_temp,
        'MaxTemp': max_temp,
        'Rainfall': rainfall,
        'Evaporation': evaporation,
        'Sunshine': sunshine,
        'WindGustDir': wind_gust_dir,
        'WindGustSpeed': wind_gust_speed,
        'WindDir9am': wind_dir_9am,
        'WindDir3pm': wind_dir_3pm,
        'WindSpeed9am': wind_speed_9am,
        'WindSpeed3pm': wind_speed_3pm,
        'Humidity9am': humidity_9am,
        'Humidity3pm': humidity_3pm,
        'Pressure9am': pressure_9am,
        'Pressure3pm': pressure_3pm,
        'Cloud9am': cloud_9am,
        'Cloud3pm': cloud_3pm,
        'Temp9am': temp_9am,
        'Temp3pm': temp_3pm,
        'RainToday': rain_today
    }

    result = predict_rain(new_input)
    st.success(f"Прогноз: {'Буде дощ' if result == 'Yes' else 'Дощу не буде'}")
