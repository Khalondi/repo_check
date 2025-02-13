import geopy.distance
import geopy.geocoders
import functools
from functools import partial
from geopy.geocoders import Nominatim
from geopy import distance
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="Mickhie's Delivery App")

geocode = partial(geolocator.geocode, language="en")
user_location=input("Enter your location: ")
user_location=geocode(user_location)
print(f"You are in, {user_location}")
location =geolocator.geocode("Bunamwaya")

def distance_calculator(address1, address2):
   
    
    if not address1 or not address2:
        return "Could not resolve your location! Try refereshing and starting again."
    
    coords_address1 =(address1.latitude, address1.longitude)
    coords_address2 = (address2.latitude, address2.longitude)
    return geodesic(coords_address2, coords_address1).kilometers


distance_result= distance_calculator(location, user_location) 
print(f"The distance between our address and your location is{distance_result:2f} kilometers.")
   
