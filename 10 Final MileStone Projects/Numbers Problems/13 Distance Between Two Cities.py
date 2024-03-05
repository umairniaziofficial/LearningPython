from haversine import haversine, Unit
import time

city1 = input("Enter the Name of the City 1: ")
city2 = input("Enter the Name of the City 2: ")

latitude1 = float(input(f"Enter the Latitude of {city1}: "))
longitude1 = float(input(f"Enter the Longitude of {city1}: "))
print("")

latitude2 = float(input(f"Enter the Latitude of {city2}: "))
longitude2 = float(input(f"Enter the Longitude of {city2}: "))
print("")

coordinates1 = (latitude1, longitude1)
coordinates2 = (latitude2, longitude2)

print(f"Finding Distance between {city1} and {city2}... ")
time.sleep(1)

choice = int(input("[1] Distance in kilometer\n[2] Distance in miles\n"))

if choice == 1:
    distance = haversine(coordinates1, coordinates2, unit=Unit.KILOMETERS)
    print(
        f"The distance between {city1} and {city2} is approximately {distance:.2f} kilometers."
    )
elif choice == 2:
    distance = haversine(coordinates1, coordinates2, unit=Unit.MILES)
    print(
        f"The distance between {city1} and {city2} is approximately {distance:.2f} miles."
    )
else:
    print("Invalid choice. Please enter 1 or 2.")
