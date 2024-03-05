import numpy as np
from scipy.spatial import distance

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def closest_pair(points):
    point_array = np.array([(point.x, point.y) for point in points])
    pairwise_distances = distance.cdist(point_array, point_array)
    np.fill_diagonal(pairwise_distances, np.inf)
    min_distance = np.min(pairwise_distances)
    return min_distance

points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3)]
min_distance = closest_pair(points)
print(f"The closest pair distance is: {min_distance}")
