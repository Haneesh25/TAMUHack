# Reads a Data File with all the Zones
# Outputs the Zone the passenger is in

# Restrictions:
# Needs a File with every calling Zones corners as coordinates
# The Polygon can be anythign with >2 sides

import matplotlib.path as mpath
from pathlib import Path

# Function to determine which polygon the point lies within
def find_containing_polygon(data_file, point):
    # Read data file and parse polygons
    polygons = []
    file_path = Path(data_file)
    with file_path.open('r') as file:
        for line in file:
            # Extract tuples from line and convert them to (float, float)
            vertices = [tuple(map(float, vertex.strip('()').split(','))) for vertex in line.split()]
            # Create a matplotlib path for the polygon
            polygons.append(mpath.Path(vertices))

    # Check which polygon contains the point
    for i, polygon in enumerate(polygons):
        if polygon.contains_point(point):
            return f"Point {point} is contained in Polygon #{i + 1}"

    return f"Point {point} is not contained in any polygon"

# Example usage:
data_filename = 'polygons.txt'
coord_x, coord_y = (5.0, 5.0)  # Point to check
result = find_containing_polygon(data_filename, (coord_x, coord_y))
print(result)
