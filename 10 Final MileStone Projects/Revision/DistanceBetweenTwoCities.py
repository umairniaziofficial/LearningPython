from geopy.geocoders import Nominatim


def GetLocation(Cityname):
    geolocator = Nominatim(user_agent="my_geocoder");
    location = geolocator.geocode(Cityname)