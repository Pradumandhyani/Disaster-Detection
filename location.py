import requests

def predict_forest_fire(latitude, longitude):
    # Construct the API URL
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=861b2fd6d9a07d6de325b77ff1b26f01"
    
    # Send a GET request to the API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract relevant parameters
        location_name = data['name']
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15  # Convert temperature from Kelvin to Celsius
        humidity = data['main']['humidity']
        wind_speed_mps = data['wind']['speed']
        weather_condition = data['weather'][0]['main']

        # Define thresholds for forest fire prediction
        temperature_threshold = 30  # Celsius
        humidity_threshold = 40     # Percentage
        wind_speed_threshold = 5     # m/s

        # Check if conditions meet forest fire prediction criteria
        if (temperature_celsius > temperature_threshold and
            humidity < humidity_threshold and
            wind_speed_mps > wind_speed_threshold):
            print(f"At {location_name}, there is a likelihood of a forest fire.")
        else:
            print(f"At {location_name}, there is no likelihood of a forest fire.")
    else:
        print("Failed to fetch weather data. Please try again.")

# Take latitude and longitude input from the user
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))

# Predict forest fire likelihood
predict_forest_fire(latitude, longitude)
