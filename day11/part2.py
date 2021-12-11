import os

flashes = 0

def flash(grid, x, y):
    grid[y][x] = 0
    global flashes
    flashes += 1

    # check left
    if (x-1) >= 0: increaseEnergy(grid, x-1, y)

    # check up
    if (y-1) >= 0: increaseEnergy(grid, x, y-1)

    # check right
    if (x+1) < len(grid[0]): increaseEnergy(grid, x+1, y)

    # check down
    if (y+1) < len(grid): increaseEnergy(grid, x, y+1)

    # check upper left
    if (y-1) >= 0 and (x-1) >= 0: increaseEnergy(grid, x-1, y-1)

    # check upper right
    if (y-1) >= 0 and (x+1) < len(grid[0]): increaseEnergy(grid, x+1, y-1)

    # check lower right
    if (y+1) < len(grid) and (x+1) < len(grid[0]): increaseEnergy(grid, x+1, y+1)

    # check lower left
    if (y+1) < len(grid) and (x-1) >= 0: increaseEnergy(grid, x-1, y+1)

def increaseEnergy(grid, x, y):
    if grid[y][x] != 0:
        if grid[y][x] < 9:
            grid[y][x] = grid[y][x] + 1
        else:
            flash(grid, x, y)

def isSynchronized(grid):
    previousEnergy = None
    for row in grid:
        for energy in row:
            if previousEnergy == None:
                previousEnergy = energy
            elif previousEnergy != energy:
                return False
    return True

grid = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

# convert to ints
for y in range(len(grid)):
    grid[y] = [int(n) for n in grid[y]]

step = 0

while not isSynchronized(grid):
    step += 1
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] = grid[y][x] + 1

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] >= 10:
                flash(grid, x, y)
   
    print(f"After step {step+1}:")
    for y in range(len(grid)):
        print(grid[y])

print(step)