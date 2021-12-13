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

def mapOutPaths(caveSystem: dict, cave: str, pathTree: dict, pathStr: str):

    if cave == 'end':
        pathTree['end'] = {}
        return

    if cave not in caveSystem:
        return

    if cave not in pathTree:
        pathTree[cave] = {}
        
    connections = caveSystem[cave]

    poppedCave = None
    if re.match('^[a-z]+$', cave):
        poppedCave = caveSystem.pop(cave)

    for connection in connections:
        mapOutPaths(caveSystem, connection, pathTree[cave], pathStr + ',' + cave)
    
    if poppedCave:
        caveSystem[cave] = poppedCave

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
mapOutPaths(caveSystem, 'start', pathTree, '')

paths = findFullPaths('', pathTree)
for path in paths:
    print(path)
print(len(paths))