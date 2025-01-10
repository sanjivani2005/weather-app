import requests
import json
import pyttsx3

# Get the city name from the user
city = input("Enter the name of the city: ")

# API URL with the city name
url = f"https://api.weatherapi.com/v1/current.json?key=94339800d009425b8c030652240307&q={city}"

# Fetch the weather data
r = requests.get(url)

# Check if the request was successful
if r.status_code == 200:
    # Print the response text
    print(r.text)

    # Convert the response text to a dictionary
    wdic = json.loads(r.text)

    # Extract the temperature in Celsius
    w = wdic["current"]["temp_c"]
    print(f"The current temperature in {city} is {w} degrees Celsius.")

    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Create the text to be spoken
    text = f"The current weather in {city} is {w} degrees Celsius."

    # Use the TTS engine to say the text
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()
else:
    print(f"Failed to get weather data for {city}. HTTP Status code: {r.status_code}")


