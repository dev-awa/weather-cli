import requests
import os
from dotenv import load_dotenv
import click
from src.cache_manager import get_cache, save_cache

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
# CLI COMMAND WITH CACHE
#===============================================
@click.command()
@click.option('--city', default='Tehran', help='City name to get weather for')
@click.option('--units', default='metric', help='Units: metric or imperial')
@click.option('--force', is_flag=True, help='Force refresh (ignore cache)')
def get_weather(city, units, force):
    """
    Get current weather for a city with caching.
    
    --force: Ignores cache and fetches fresh data from API 
    """

    #===========================================
    # CHECK CACHE FIRST
    #===========================================
    # If --force is NOT used, try to get cached data
    if not force:
        cached_data = get_cache(city)
        if cached_data:
            # Found valid cached data, display it
            display_weather(cached_data, city, from_cache=True)
            return

    #===========================================
    # FETCH FROM API (CACHE MISS OR FORCE)
    #===========================================
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"
    
    try:
        response = requests.get(url)
        data = response.json()
    
        if response.status_code == 200:
            # Save to cache for future use
            save_cache(city, data)
            display_weather(data, city, from_cache=False)    
        else:
            click.echo(f"❌ Error: {data.get('message', 'Unknown error')}")
            
    except Exception as e:
        click.echo(f"❌ Connection error: {e}")

#=======================================================
# DISPLAY WEATHER DATA
#=======================================================
def display_weather(data, city, from_cache=False):
    """
    Display weather data in a nice format.
    
    Args:
        data (dict): Weather data from API or cache
        city (str): City name
        from_cache (bool): True if data came from cache
    """
    
    # Add indicator if data is from cache
    cache_msg = " (from cache)" if from_cache else ""
    
    click.echo(f"City: {data['name']}, {data['sys']['country']}{cache_msg}")
    click.echo(f"Temp: {data['main']['temp']}°C")
    click.echo(f"Feels like: {data['main']['feels_like']}°C")
    click.echo(f"Weather: {data['weather'][0]['description']}")
    click.echo(f"Humidity: {data['main']['humidity']}%")
    click.echo(f"Wind: {data['wind']['speed']} km/h")

#=======================================================
# ENTRY POINT
#=======================================================
if __name__ == "__main__":
    get_weather()