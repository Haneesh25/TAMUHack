import heapq
import math

# Provided pixel coordinates for known locations
pixel_coords = {
    'A8': (284, 288),
    'Einstein Bros. Bagels North': (961, 423),
    'A10': (1474, 416)
}

# Provided GPS coordinates for known locations
gps_coords = {
    'A8': (32.907142, -97.038825),
    'Einstein Bros. Bagels North': (32.907012, -97.038149),
    'A10': (32.907026, -97.037662)
}

# Calculate scale factors for longitude and latitude
pixel_distance_x = pixel_coords['A10'][0] - pixel_coords['A8'][0]
gps_diff_lon = gps_coords['A10'][1] - gps_coords['A8'][1]
scale_factor_lon = pixel_distance_x / gps_diff_lon

pixel_distance_y = pixel_coords['Einstein Bros. Bagels North'][1] - pixel_coords['A8'][1]
gps_diff_lat = gps_coords['Einstein Bros. Bagels North'][0] - gps_coords['A8'][0]
scale_factor_lat = pixel_distance_y / gps_diff_lat

# Functions to estimate GPS coordinates from pixel coordinates and vice versa
def estimate_gps_from_pixels(pixel_x, pixel_y, ref_gps, ref_pixel, scale_factors):
    pixel_x_diff = (pixel_x - ref_pixel[0]) / scale_factors['lon']
    pixel_y_diff = (pixel_y - ref_pixel[1]) / scale_factors['lat']
    estimated_gps_lat = ref_gps[0] + pixel_y_diff
    estimated_gps_lon = ref_gps[1] + pixel_x_diff
    return (estimated_gps_lat, estimated_gps_lon)

def estimate_pixels_from_gps(gps_lat, gps_lon, ref_gps, ref_pixel, scale_factors):
    pixel_x_diff = (gps_lon - ref_gps[1]) * scale_factors['lon']
    pixel_y_diff = (gps_lat - ref_gps[0]) * scale_factors['lat']
    estimated_pixel_x = ref_pixel[0] + pixel_x_diff
    estimated_pixel_y = ref_pixel[1] + pixel_y_diff
    return (int(estimated_pixel_x), int(estimated_pixel_y))

# Reference GPS and pixel coordinates (using A8 as the reference point)
ref_gps_coords = gps_coords['A8']
ref_pixel_coords = pixel_coords['A8']
scale_factors = {'lon': scale_factor_lon, 'lat': scale_factor_lat}

# A* algorithm for pathfinding
def heuristic(node, goal):
    return 0

def a_star_search_dynamic(graph, start, goal, heuristic_func):
    queue = [(0, start, 0, [start])]
    visited = set()
    while queue:
        cost, node, path_cost, path = heapq.heappop(queue)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        neighbors = graph[node] if node in graph else graph['Person'] if node == 'Person' else []
        for neighbor, edge_cost in neighbors:
            if neighbor not in visited:
                heapq.heappush(queue, (path_cost + edge_cost + heuristic_func(neighbor, goal),
                                       neighbor, path_cost + edge_cost, path + [neighbor]))
    return None

# Graph of the map with nodes and edges
graph = {
    'A8': [('A9', 1)],  # Example edges, should be updated with actual connections
    'A9': [('A8', 1)],  # Example edges
    # ... (Add other nodes and edges)
}

# Functions to estimate directions
def estimate_direction_gps(current, next_node, scale_factors):
    current_gps = estimate_gps_from_pixels(node_coordinates[current][0], node_coordinates[current][1], 
                                           ref_gps_coords, ref_pixel_coords, scale_factors)
    next_gps = estimate_gps_from_pixels(node_coordinates[next_node][0], node_coordinates[next_node][1], 
                                        ref_gps_coords, ref_pixel_coords, scale_factors)
    direction_radians = math.atan2(next_gps[1] - current_gps[1], next_gps[0] - current_gps[0])
    direction_degrees = math.degrees(direction_radians)
    cardinal_directions = ["north", "northeast", "east", "southeast", 
                           "south", "southwest", "west", "northwest", "north"]
    index = int((direction_degrees + 22.5) // 45)
    return cardinal_directions[index]

def create_advanced_directions(path, scale_factors):
    directions = ["Start at " + path[0] + "."]
    for i in range(len(path) - 1):
        direction = estimate_direction_gps(path[i], path[i+1], scale_factors)
        directions.append(f"From {path[i]}, head {direction} towards {path[i+1]}.")
    directions.append("You have arrived at your destination.")
    return directions

# Example usage
person_gps_coords = (32.907073, -97.038208)  # GPS coordinates of the person
person_pixel_coords = estimate_pixels_from_gps(person_gps_coords[0], person_gps_coords[1], 
                                               ref_gps_coords, ref_pixel_coords, scale_factors)
graph['Person'] = [('Einstein Bros. Bagels North', 1), ('A8', 1)]  # Connect the person to the graph
destination_node = 'A9'  # Destination node
path_to_destination = a_star_search_dynamic(graph, 'Person', destination_node, heuristic)
directions_to_destination = create_advanced_directions(path_to_destination, scale_factors)
