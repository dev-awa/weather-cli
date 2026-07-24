import requests
import os
from dotenv import load_dotenv
import click
from src.cache_manager import get_cache, save_cache
from colorama import init, Fore, Style

# ============================================
# INITIALIZE COLORAMA
# ============================================
# init() enables color support on Windows
init(autoreset=True)

# ============================================
# LOAD ENVIRONMENT VARIABLES
# ============================================
load_dotenv()

# ============================================
# GET API KEY
# ============================================
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    print("❌ Error: API_KEY not found")
    exit(1)

# ============================================
# CLI COMMAND WITH CACHE AND COLORS
# ============================================
@click.command()
@click.option('--city', default='Tehran', help='City name to get weather for')
@click.option('--units', default='metric', help='Units: metric or imperial')
@click.option('--force', is_flag=True, help='Force refresh (ignore cache)')
def get_weather(city, units, force):
    """
    Get current weather for a city with caching and colored output.
    """
    
    # Check cache first
    if not force:
        cached_data = get_cache(city)
        if cached_data:
            display_weather(cached_data, city, from_cache=True)
            return
    
    # Fetch from API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            save_cache(city, data)
            display_weather(data, city, from_cache=False)
        else:
            # Red color for errors
            click.echo(f"{Fore.RED}❌ Error: {data.get('message', 'Unknown error')}")
            
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Connection error: {e}")

# ============================================
# DISPLAY WEATHER DATA WITH COLORS
# ============================================
def display_weather(data, city, from_cache=False):
    """
    Display weather data in a nice format with colors.
    
    Fore.CYAN: For labels
    Fore.WHITE: For values
    Fore.YELLOW: For cache indicator
    Style.RESET_ALL: Reset color to default
    """
    
    # Yellow color for cache indicator
    cache_msg = f" {Fore.YELLOW}(from cache){Style.RESET_ALL}" if from_cache else ""
    
    # Print with colors
    click.echo(f"\n{Fore.CYAN}🌍 City: {Fore.WHITE}{data['name']}, {data['sys']['country']}{cache_msg}")
    click.echo(f"{Fore.CYAN}🌡️  Temp: {Fore.WHITE}{data['main']['temp']}°C")
    click.echo(f"{Fore.CYAN}🌡️  Feels like: {Fore.WHITE}{data['main']['feels_like']}°C")
    click.echo(f"{Fore.CYAN}☁️  Weather: {Fore.WHITE}{data['weather'][0]['description'].title()}")
    click.echo(f"{Fore.CYAN}💧 Humidity: {Fore.WHITE}{data['main']['humidity']}%")
    click.echo(f"{Fore.CYAN}💨 Wind: {Fore.WHITE}{data['wind']['speed']} km/h\n")

# ============================================
# ENTRY POINT
# ============================================
if __name__ == "__main__":
    get_weather()