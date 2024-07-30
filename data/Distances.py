import googlemaps
import pandas as pd
from datetime import datetime

# Initialize Google Maps API client
api_key = 'AIzaSyCo4GeEU4Iu7Y_wjpypux-7WqQrZgH1OHE'
gmaps = googlemaps.Client(key=api_key)

# List of cities and reference points
cities = [
    "Ann Arbor, MI",
    "Detroit, MI",
    "Columbus, OH",
    "Cincinnati, OH",
    "Dayton, OH",
    "Guelph, ON",
    "London, ON",
    "Cambridge, ON",
    "Kitchener, ON",
    "Vaughan, ON"
]

reference_points = ["Guelph, ON", "St. Henry, OH"]

# Function to get driving distance
def get_driving_distance(origin, destination):
    result = gmaps.distance_matrix(origins=origin, destinations=destination, mode="driving", departure_time=datetime.now())
    distance = result['rows'][0]['elements'][0]['distance']['text']
    return distance

# Prepare a DataFrame to store results
results = []

# Calculate distances
for city in cities:
    for point in reference_points:
        distance = get_driving_distance(city, point)
        results.append({'City': city, 'Reference Point': point, 'Distance': distance})

# Create a DataFrame from the results
df = pd.DataFrame(results)
print(df)