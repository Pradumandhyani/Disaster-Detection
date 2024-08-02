# app.py

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def predict_forest_fire(latitude, longitude):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=861b2fd6d9a07d6de325b77ff1b26f01"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        location_name = data['name']
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        humidity = data['main']['humidity']
        wind_speed_mps = data['wind']['speed']

        temperature_threshold = 30
        humidity_threshold = 40
        wind_speed_threshold = 5

        if (temperature_celsius > temperature_threshold and
            humidity < humidity_threshold and
            wind_speed_mps > wind_speed_threshold):
            return f"At {location_name}, there is a likelihood of a forest fire."
        else:
            return f"At {location_name}, there is no likelihood of a forest fire."
    else:
        return "Failed to fetch weather data. Please try again."

@app.route('/')
def index():
    return render_template('flaskk.html')

@app.route('/predict', methods=['POST'])
def predict():
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])
    prediction = predict_forest_fire(latitude, longitude)
    return prediction

if __name__ == '__main__':
    app.run(debug=True)
