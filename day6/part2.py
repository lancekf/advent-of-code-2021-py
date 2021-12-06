import os
import sys

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

def add(groups: dict, remainingDays: int, count: int) -> None:
    if (remainingDays not in groups):
        groups[remainingDays] = 0
    groups[remainingDays] = groups[remainingDays] + count


days = int(sys.argv[1])

# group by remaining days
fish = {}
for s in input[0].split(','):
    add(fish, int(s), 1)

for day in range(days):
    nextDay = {}
    for remainingDays, count in fish.items():
        if (remainingDays == 0):
            add(nextDay, 8, count)
            add(nextDay, 6, count)
        else:
            add(nextDay, remainingDays-1, count)
    fish = nextDay

sum = 0
for school, count in fish.items(): sum += count

print(sum)