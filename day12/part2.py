import os
import re

def parseInputToCaveSystem(input):
    caveSystem = {}
    for line in input:
        split = line.split('-')
        addConnectionToCave(caveSystem, split[0], split[1])
        addConnectionToCave(caveSystem, split[1], split[0])
    
    return caveSystem

def addConnectionToCave(caveSystem: dict, cave: str, connection: str):
    if cave != 'end' and connection != 'start':
        if cave not in caveSystem:
            caveSystem[cave] = set()
        caveSystem[cave].add(connection)

def isSmallCave(cave):
    return re.match('^[a-z]+$', cave)

def getMaxSmallCaveCount(path: list) -> int:
    counts = {}
    max = None
    for cave in path:
        if isSmallCave(cave):
            if cave not in counts:
                counts[cave] = 0
            count = counts[cave] + 1
            counts[cave] = count
            if not max or count > max:
                max = count
    return max

def mapOutPaths(caveSystem: dict, cave: str, pathTree: dict, path: list):
    if cave == 'end':
        pathTree['end'] = {}
        return

    if cave not in caveSystem:
        return

    if isSmallCave(cave):
        maxCount = getMaxSmallCaveCount(path)
        if maxCount == 2 and cave in path:
            return

    # extend path
    pathTree[cave] = {}
    path.append(cave)

    connections = caveSystem[cave]

    for connection in connections:
        mapOutPaths(caveSystem, connection, pathTree[cave], path.copy())

def findFullPaths(parentPath: str, pathTree: dict):
    paths = []
    if not pathTree:
        if parentPath.endswith('end'):
            paths.append(parentPath)
    else:
        for cave in pathTree:
            paths.extend(findFullPaths(parentPath + "," + cave, pathTree[cave]))
    
    return paths
    
input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

caveSystem = parseInputToCaveSystem(input)
print(caveSystem)

pathTree = {}
mapOutPaths(caveSystem, 'start', pathTree, [])

paths = findFullPaths('', pathTree)
sorted(paths)
for path in paths:
    print(path)
print(len(paths))