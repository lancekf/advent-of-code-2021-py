import os
import sys

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

days = int(sys.argv[1])

fishies = [int(n) for n in input[0].split(',')]

for day in range(days):
    newFish = []
    for i in range(len(fishies)):
        fish = fishies[i]
        if (fish == 0):
            newFish.append(8)
            fishies[i] = 6
        else:
            fishies[i] = fish - 1
    
    fishies.extend(newFish)

print(len(fishies))