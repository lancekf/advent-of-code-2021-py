import os

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

def markLine(graph: list, start: list, end: list) -> None:
    x = start[0]
    y = start[1]
    
    while (x != end[0] or y != end[1]):
        markPoint(graph, x, y)
        x = traverse(x, end[0])
        y = traverse(y, end[1])

    markPoint(graph, x, y)

def markPoint(graph: list, x: int, y: int) -> None:
    # grow map as necessary
    while len(graph) <= y: graph.append([])
    row = graph[y]

    while len(row) <= x: row.append(0)
    row[x] = row[x] + 1 # increment count

def traverse(start: int, end: int) -> int:
    if (start < end):
        return start+1
    elif end < start:
        return start-1
    else:
        return start

graph = []
for row in input:
    print(row)
    points = row.split(" -> ")
    start = [int(n) for n in points[0].split(",")]
    end = [int(n) for n in points[1].split(",")]

    markLine(graph, start, end)

intersections = 0
for row in graph:
    print(row)
    for point in row:
        if point > 1:
            intersections += 1

print(f"intersections: {intersections}")
