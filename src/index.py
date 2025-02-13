import geopy.distance
import geopy.geocoders
import functools
from functools import partial
from geopy.geocoders import Nominatim
from geopy import distance
from geopy.distance import Distance

geolocator = Nominatim(user_agent="Mickhie's Delivery App")

geocode = partial(geolocator.geocode, language="en")
user_location=input("Enter your location: ")
print(geocode(user_location))
location =geolocator.reverse("0.264913, 32.546467")
print(location.address)

def distance_calculator(address1, address2):
    address1=geocode(user_location)
    address2=geocode(location)
    distance=(geopy.distance.distance(address2,address1))
   
    return distance
print(f"The distance between our address and your location is{distance_calculator} kilometers.")
   
