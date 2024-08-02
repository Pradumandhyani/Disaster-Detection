import pandas as pd

# Load your dataset
data = pd.read_csv("IndianWeatherRepository.csv")

def detect_forest_fire(country, location_name, region):
    # Filter the dataset based on user input
    filtered_data = data[(data['country'] == country) & 
                         (data['location_name'] == location_name) & 
                         (data['region'] == region)]

    if filtered_data.empty:
        print("No data found for the specified country, location, and region.")
        return

    # Extract relevant features for predicting forest fires
    temperature_celsius = filtered_data['temperature_celsius'].iloc[0]
    humidity = filtered_data['humidity'].iloc[0]
    condition_text = filtered_data['condition_text'].iloc[0].lower()
    wind_mph = filtered_data['wind_mph'].iloc[0]

    # Define thresholds or conditions for determining forest fire risk
    temperature_threshold = 25  # Celsius
    humidity_threshold = 60     # Percentage
    wind_speed_threshold = 10   # mph
    condition_keywords = ['fire', 'smoke']

    # Check if the extracted features indicate a likelihood of forest fire
    if (temperature_celsius > temperature_threshold and 
        humidity < humidity_threshold and 
        wind_mph > wind_speed_threshold) or any(keyword in condition_text for keyword in condition_keywords):
        print("There is a likelihood of a forest fire.")
    else:
        print("There is no likelihood of a forest fire.")

# Take input from the user
country = input("Enter country name: ")
location_name = input("Enter location name: ")
region = input("Enter region: ")

# Call the function to detect forest fire
detect_forest_fire(country, location_name, region)
