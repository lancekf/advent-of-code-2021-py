import os

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

def parseInputIntoGrid(input):
    grid = []

    for line in input:
        grid.append([int(n) for n in line])

    return grid

def isLowPoint(grid, x, y):
    point = grid[y][x]

    # check left
    if x > 0 and point >= grid[y][x-1]:
        return False

    # check up
    if y > 0 and point >= grid[y-1][x]:
        return False
    
    # check right
    if x < (len(grid[y])-1) and point >= grid[y][x+1]:
        return False
    
    # check down
    if y < (len(grid)-1) and point >= grid[y+1][x]:
        return False
    
    return True

grid = parseInputIntoGrid(input)

riskLevel = 0

print(f"Grid height: {len(grid)}")
print(f"Grid width: {len(grid[0])}")

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if isLowPoint(grid, x, y):
            riskLevel += (1 + grid[y][x])

print(riskLevel)