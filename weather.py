import requests
import os
from dotenv import load_dotenv

#===============================================
# LOAD ENVIRONMENT VARIABLES
#===============================================
load_dotenv()

#===============================================
# Get API KEY
#===============================================
API_KEY = os.getenv('API_KEY')

#===============================================
# VALIDATE API KEY
#===============================================
# Check if API_KEY exists, if not show error
if not API_KEY:
    print("Error: API_KEY not found")
    exit(1)

#===============================================
# SET CITY AND BUILD URL
#===============================================
# City name to get weather for
city = "Tehran"

# Build the API URL with:
# - city name
# - API key
# -units=metric (Celsius)
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

#===============================================
# SEND HTTP REQUEST TO API
#===============================================
try:
    # requests.get() send a Get request to the URL
    response = requests.get(url)
    
    # .json() parses the response from JSON to Python dictionary
    data = response.json()
    
    #===============================================
    # CHECK RESPONSE STATUS
    #===============================================
    # 200 means success
    if response.status_code == 200:
        # Display weather data from the response
        print(f"City: {data['name']}, {data['sys']['country']}")
        print(f"Temp: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind: {data['wind']['speed']} km/h")
    else:
        # Show error message from API
        print(f"Error: {data.get('message', 'Unknown error')}")

except Exception as e:
    # Catch any connection errors
    print(f"Connection error: {e}")