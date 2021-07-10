import random

n = int(input())
points = []
for i in range(0, n):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    print(x, y)
