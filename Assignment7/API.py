import requests
import os
from dotenv import load_dotenv

load_dotenv()

class GeoLocation:
   
    API_KEY = os.getenv("OPENCAGE_API_KEY")
    BASE_URL = os.getenv("OPENCAGE_API_URL")

    @staticmethod
    def get_coordinates(place_name):
        
        api_url_params = {
            "q": place_name,
            "key": GeoLocation.API_KEY
        }

        return GeoLocation.handle_get_coordinates(api_url_params)


    @staticmethod
    def handle_get_coordinates(api_url_params):
        try:
            response = requests.get(GeoLocation.BASE_URL, params=api_url_params)
            response.raise_for_status()
            data = response.json()
            
            latitude, longitude = GeoLocation.fetch_lat_lon_from_response(data) 

        except requests.RequestException as error:
            print(f"API error: {error}")
        
        return latitude, longitude
    
    
    @staticmethod
    def fetch_lat_lon_from_response(data):
        latitude = None
        longitude = None
        
        if data['results']:
            latitude = data['results'][0]['geometry']['lat']
            longitude = data['results'][0]['geometry']['lng']
        
        return latitude, longitude
