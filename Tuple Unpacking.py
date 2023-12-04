import math
points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]
map = 0
distance = list(range(len(points)))
print(distance)
for (x,y) in points:
    distance[map] = math.sqrt((x**2) + (y**2))
    map += 1
print(min(distance))

