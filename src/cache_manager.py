import os
import json
import time

#================================================
# CACHE CONFIGURATION
#================================================
# Directory where cache files will be stored
CACHE_DIR = "cache"

# How long cache is valid (in seconds)
# 600 seconds = 10 minutes
CACHE_DURATION = 600 # 10 minutes

#================================================
# CREATE CACHE DIRECTORY
#================================================
# Check if cache directory exists, if not create it
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

#================================================
# GET CACHED DATA
#================================================
def get_cache(city):
    """
    Retrieve cached weather data for a city.
    
    Args:
        city (str): Name of the city
        
    Returns:
        dict or None: Cached weather data if valid, else None.
    """
    # Create filename from city name (lowercase for consistency)
    cache_file = os.path.join(CACHE_DIR, f"{city.lower()}.json")
    
    # Check if cache file exists
    if os.path.exists(cache_file):
        # Open and read the cache file
        with open(cache_file, 'r') as f:
            data = json.load(f)
            
            # Check if cache is still valid
            # Compare current time with timestamp when data was cached
            if time.time() - data['timestamp'] < CACHE_DURATION:
                # Cache is still fresh, return the weather data
                return data['weather']
    
    # Cache doesn't exist or expired
    return None

#================================================
# SAVE DATA TO CACHE
#================================================
def save_cache(city, weather_data):
    """
    Save weather data to cache.
    
    Args:
        city (str): Name of the city
        weather_data (dict): Weather data from API
    """
    
    # Create filename from city name
    cache_file = os.path.join(CACHE_DIR, f"{city.lower()}.json")
    
    # Save data with timestamp
    with open(cache_file, 'w') as f:
        json.dump({
            'timestamp': time.time(), # Current time
            'weather': weather_data   # Weather data
        }, f)