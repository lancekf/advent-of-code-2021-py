import os

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

horizontal = 0
depth = 0
aim = 0

for step in input:
    s = step.split()
    distance = int(s[1])
    if s[0] == 'forward':
        horizontal = horizontal + distance
        depth = depth + (aim * distance)
    elif s[0] == 'up':
        aim = aim - distance
    elif s[0] == 'down':
        aim = aim + distance
    
    print('{0},{1},{2} - {3}'.format(horizontal, depth, aim, step))

print(horizontal*depth)

print(dir)