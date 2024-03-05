from geopy.geocoders import Nominatim
import haversine

def GeoLocation(city_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(city_name)
    
    if location: 
        latitude = location.latitude
        longitude = location.longitude
        return (latitude, longitude)
    
    return False

def FindDistance(cities):
    city1 = GeoLocation(cities[0])
    city2 = GeoLocation(cities[1])
    
    if city1 and city2:
        total_distance = haversine.haversine(city1, city2)
        return total_distance
    else:
        return "Location not found for one or both cities."

if __name__ == "__main__":
    city1 = input("Name of City1: ")
    city2 = input("Name of City2: ")
    
    print("Finding Distance between 2 Cities...")
    cities = (city1, city2)
    the_distance = FindDistance(cities)
    
    print(f"The Distance Between {city1} and {city2} is: {the_distance} Km")
