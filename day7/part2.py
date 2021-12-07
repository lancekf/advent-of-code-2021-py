import os

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

positions = [int(n) for n in input[0].split(',')]

min = min(positions)
max = max(positions)
cheapest = None

for end in range(min, max):
    total = 0
    for start in positions:
        distance = abs(end-start)
        total += (distance*(distance+1))/2

    if (cheapest == None or total < cheapest):
        cheapest = total

print(cheapest)