import math
import sys
import matplotlib.pyplot as plt
from datetime import datetime


def cost(p0, r):  # a function to calculate the total length of the route
    total_dist = 0
    total_dist += math.sqrt((r[0][0] - p0[0])**2 + ((r[0][1] - p0[1])**2))
    total_dist += math.sqrt((r[len(r) - 1][0] - p0[0])**2 + ((r[len(r) - 1][1] - p0[1])**2))
    for i in range(1, len(r)):
        total_dist += math.sqrt((r[i][0] - r[i - 1][0])**2 + ((r[i][1] - r[i - 1][1])**2))
    return total_dist


# ----------------------------------------------------------------------------------------------------------------------
# getting the inputs
n = int(input())
c = input().split(' ')
x0 = int(c[0])
y0 = int(c[1])
p0 = [x0, y0]
points = []
for i in range(1, n):
    c = input().split(' ')
    x = int(c[0])
    y = int(c[1])
    points.append([x, y, False])

# ----------------------------------------------------------------------------------------------------------------------
# start time
t1 = datetime.now()

# ----------------------------------------------------------------------------------------------------------------------
# Nearest-Neighbor algorithm
route = []
current_point = p0
for step in range(0, len(points)):
    min_dist = sys.maxsize
    min_index = -1
    for i in range(0, len(points)):
        if points[i][2]:  # if visited before
            continue
        dist = math.sqrt((points[i][0] - current_point[0])**2 + ((points[i][1] - current_point[1])**2))
        if dist < min_dist:
            min_index = i
            min_dist = dist
    points[min_index][2] = True  # setting to visited
    route.append([points[min_index][0], points[min_index][1]])

print(p0, route, p0)
print(cost(p0, route))

# ----------------------------------------------------------------------------------------------------------------------
# end time
t2 = datetime.now()
print(t2 - t1)
# ----------------------------------------------------------------------------------------------------------------------
# plotting the route
plt.plot([p0[0], route[0][0]], [p0[1], route[0][1]], marker='o')
plt.plot([p0[0], route[len(route) - 1][0]], [p0[1], route[len(route) - 1][1]], marker='o')
for i in range(1, len(route)):
    plt.plot([route[i - 1][0], route[i][0]], [route[i - 1][1], route[i][1]], marker='o')
plt.show()
