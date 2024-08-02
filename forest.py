import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load your dataset
data = pd.read_csv("forestfires.csv")

# Convert the target variable to binary format
data['fire_occurred'] = (data['area'] > 0).astype(int)

X = data[['FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain']]
y = data['fire_occurred']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression()
model.fit(X_scaled, y)

# Take input from the user
print("Enter the values for the following features:")
FFMC = float(input("FFMC (Fine Fuel Moisture Code): "))
DMC = float(input("DMC (Duff Moisture Code): "))
DC = float(input("DC (Drought Code): "))
ISI = float(input("ISI (Initial Spread Index): "))
temp = float(input("Temperature: "))
RH = float(input("Relative Humidity: "))
wind = float(input("Wind Speed: "))
rain = float(input("Rainfall: "))

# Scale the user input
user_input_scaled = scaler.transform([[FFMC, DMC, DC, ISI, temp, RH, wind, rain]])

# Predict whether there can be a forest fire or not
prediction = model.predict(user_input_scaled)

if prediction == 1:
    print("There is a likelihood of forest fire.")
else:
    print("There is no likelihood of forest fire.")
