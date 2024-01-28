# Takes in 2 sets of coordinates (Current and Destination)
# Outputs the Distance + Time 

from math import radians, sin, cos, sqrt, atan2

# Function to calculate estimated walking time between two coordinates
def calculate_walking_time(coord1x, coord1y, coord2x, coord2y):
    # Earth's radius in meters
    R = 6371000

    # Convert latitude and longitude values from degrees to radians
    lat1, lon1 = map(radians, [coord1x, coord1y])
    lat2, lon2 = map(radians, [coord2x, coord2y])

    # Calculate differences between coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula to calculate distance
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate distance in meters
    distance = R * c

    # Average walking speed is 1 meter per second
    walking_speed = 1

    # Calculate estimated walking time in seconds
    walking_time_seconds = distance / walking_speed

    # Convert walking time to a more readable format (hours, minutes, seconds)
    hours = walking_time_seconds // 3600
    minutes = (walking_time_seconds % 3600) // 60
    seconds = walking_time_seconds % 60

    return hours, minutes, seconds

# Example usage:
coord1x = 41.49008   # Latitude of starting point
coord1y = -71.312796 # Longitude of starting point
coord2x = 41.499498  # Latitude of ending point
coord2y = -81.695391 # Longitude of ending point

hours, minutes, seconds = calculate_walking_time(coord1x, coord1y, coord2x, coord2y)
print(f"The estimated walking time between the two coordinates is: {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds")
