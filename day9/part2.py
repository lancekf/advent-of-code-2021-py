import os

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

def parseInputIntoGrid(input):
    grid = []

    for line in input:
        grid.append([int(n) for n in line])

    return grid

def findLowPoints(grid):
    lowPoints = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if isLowPoint(grid, x, y):
                lowPoints.append((x, y))
    
    return lowPoints

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

def findBasinPoints(grid, basinPoints, x, y):
    num = grid[y][x]
    basinPoints.append((x, y))

    # check left
    if x > 0 and num < grid[y][x-1] < 9 and (x-1, y) not in basinPoints:
        findBasinPoints(grid, basinPoints, x-1, y)

    # check up
    if y > 0 and num < grid[y-1][x] < 9 and (x, y-1) not in basinPoints:
        findBasinPoints(grid, basinPoints, x, y-1)
    
    # check right
    if (x+1) < (len(grid[y])) and num < grid[y][x+1] < 9 and (x+1, y) not in basinPoints:
        findBasinPoints(grid, basinPoints, x+1, y)
    
    # check down
    if (y+1) < len(grid) and num < grid[y+1][x] < 9 and (x, y+1) not in basinPoints:
        findBasinPoints(grid, basinPoints, x, y+1)
    
    return basinPoints

grid = parseInputIntoGrid(input)

print(f"Grid height: {len(grid)}")
print(f"Grid width: {len(grid[0])}")

lowPoints = findLowPoints(grid)

print(f"low points: {lowPoints}")

basinSizes = []
for point in lowPoints:
    basinPoints = findBasinPoints(grid, [], point[0], point[1])
    basinSizes.append(len(basinPoints))

basinSizes = sorted(basinSizes)

print(basinSizes[-3:])
answer = 1
for size in basinSizes[-3:]:
    answer = answer * size

print(answer)