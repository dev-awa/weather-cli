import requests
import os
from dotenv import load_dotenv
import click

#===============================================
# LOAD ENVIRONMENT VARIABLES
#===============================================
load_dotenv()

#===============================================
# Get API KEY
#===============================================
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    print("Error: API_KEY not found")
    exit(1)

#===============================================
# CLI COMMAND WITH CLICK
#===============================================
# @click.command() mekes this function a CLI command
# @click.option() adds command-line options
# --city: city name (default: Tehran)
# --units: metric or imperial (default: metric)
@click.command()
@click.option('--city', default='Tehran', help='City name to get weather for')
@click.option('--units', default='metric', help='Units: metric or imperial')
def get_weather(city, units):
    """
    Get current weather for a city.
    
    This function is called when the user runs the script.
    It takes city and units as parameters from command line. 
    """

    #===========================================
    # BUILD URL WITH PARAMETERS
    #===========================================
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"
    
    #===============================================
    # SEND HTTP REQUEST TO API
    #===============================================
    try:
        response = requests.get(url)
        data = response.json()
    
        #===============================================
        # CHECK RESPONSE STATUS
        #===============================================
        if response.status_code == 200:
            # Display weather data
            # click.echo() is like print() but works better with CLI
            click.echo(f"City: {data['name']}, {data['sys']['country']}")
            click.echo(f"Temp: {data['main']['temp']}°C")
            click.echo(f"Feels like: {data['main']['feels_like']}°C")
            click.echo(f"Weather: {data['weather'][0]['description']}")
            click.echo(f"Humidity: {data['main']['humidity']}%")
            click.echo(f"Wind: {data['wind']['speed']} km/h")
        else:
            click.echo(f"Error: {data.get('message', 'Unknown error')}")

    except Exception as e:
        print(f"Connection error: {e}")

#=======================================================
# ENTRY POINT
#=======================================================
# This runs the get_weather() function when script is executed
if __name__ == "__main__":
    get_weather()