import os

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

positions = [int(n) for n in input[0].split(',')]
cheapest = None

for end in range(min(positions), max(positions)):
    total = 0
    for start in positions: total += abs(end-start)

    if (cheapest == None or total < cheapest):
        cheapest = total

print(cheapest)