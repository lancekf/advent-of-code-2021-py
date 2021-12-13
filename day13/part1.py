import os

def getGridAndFolds():
    input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

    folding = False
    grid = []
    folds = []
    for line in input:
        print(line)
        if not line:
            folding = True
        elif folding:
            split = line.split(' ')[2].split('=')
            if split[0] == 'x':
                folds.append((int(split[1]), 0))
            else:
                folds.append((0, int(split[1])))
        else:
            split = [int(n) for n in line.split(',')]
            setCoordinateTo(grid, split[0], split[1], '#', '.')
    
    return (grid, folds)

def setCoordinateTo(grid, x, y, defaultValue, pad):
    row = None
    if y == None:
        row = grid
    else:
        diff = y-len(grid)+1
        if diff > 0:
            for i in range(diff):
                grid.append([])

        row = grid[y]
    diff = x-len(row)+1
    if diff > 0:
        for i in range(diff):
            row.append(pad)

    if row[x] == pad:
        row[x] = defaultValue

def foldGrid(grid, fold):
    if fold[0]:
        leftGrid = []
        for y in range(len(grid)):
            row = grid[y]
            left = row[:fold[0]]
            right = row[fold[0]+1:]
            for x in range(len(right)):
                setCoordinateTo(left, len(left)-x-1, None, right[x], '.')
            leftGrid.append(left)
        return leftGrid
    if fold[1]:
        top = grid[:fold[1]]
        bottom = grid[fold[1]+1:]
        for y in range(len(bottom)):
            for x in range(len(bottom[y])):
                setCoordinateTo(top, x, len(top)-y-1, bottom[y][x], '.')
        return top

def printGrid(grid):
    print('GRID START')
    for row in grid:
        print(row)
    print('GRID END')

def countDots(grid):
    count = 0
    for row in grid:
        count += row.count('#')
    return count

result = getGridAndFolds()
grid = result[0]
folds = result[1]

# printGrid(grid)
for fold in folds:
    grid = foldGrid(grid, fold)
    # printGrid(grid)
    print(f"Dots: {countDots(grid)}")