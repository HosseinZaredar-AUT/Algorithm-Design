import itertools
import sys
import math
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
    points.append([x, y])


# ----------------------------------------------------------------------------------------------------------------------
# start time
t1 = datetime.now()

# ----------------------------------------------------------------------------------------------------------------------
# finding all the permutations
per = list(itertools.permutations(points))

# ----------------------------------------------------------------------------------------------------------------------
# Exhaustive search algorithm
min_cost = sys.maxsize
min_index = -1
for i in range(0, len(per)):
    cst = cost(p0, per[i])
    if cst < min_cost:
        min_cost = cst
        min_index = i
print(p0, per[min_index], p0)
print(cost(p0, per[min_index]))

# ----------------------------------------------------------------------------------------------------------------------
# end time
t2 = datetime.now()
print(t2 - t1)
# ----------------------------------------------------------------------------------------------------------------------
# plotting the route
plt.plot([p0[0], per[min_index][0][0]], [p0[1], per[min_index][0][1]], marker='o')
plt.plot([p0[0], per[min_index][len(per[min_index]) - 1][0]],
         [p0[1], per[min_index][len(per[min_index]) - 1][1]], marker='o')
for i in range(1, len(per[min_index])):
    plt.plot([per[min_index][i - 1][0], per[min_index][i][0]],
             [per[min_index][i - 1][1], per[min_index][i][1]], marker='o')
plt.show()

