import os
from dotenv import load_dotenv

#===============================================
# LOAD ENVIRONMENT VARIABLES
#===============================================
# load_dotenv() reads the .env file and loads
# all variables into environment
load_dotenv()

#===============================================
# Get API KEY FROM ENVIRONMENT
#===============================================
# os.getenv() retrieves the value of API_KEY
# from the environment variables
API_KEY = os.getenv('API_KEY')

#===============================================
# VALIDATE API KEY
#===============================================
# Check if API_KEY exists, if not show error
if not API_KEY:
    print("Error: API_KEY not found in .env file")
    print("Please add your API key to .env file")
else:
    # Show first 5 characters to confirm it's loadded
    print("API_KEY loadded successfully!")
    print(f"Your API Key: {API_KEY[:5]}...")