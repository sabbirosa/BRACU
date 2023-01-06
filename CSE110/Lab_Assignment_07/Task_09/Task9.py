import math

points = [(1,7), (4,5), (-1,7), (-2,0), (1,1), (5,-1)]
min_points = (points[0])
x, y = min_points
min_distance = math.sqrt(x**2 + y**2)

for i in points:
  x, y = i
  distance = math.sqrt(x**2 + y**2)
  if distance < min_distance:
    min_distance = distance
    min_points = (x, y)

print("Minimum distance =", min_distance)
print("Here the closest point is", min_points, "which has a distance of", min_distance, "from the origin.")