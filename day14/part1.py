import os

class Node:
    def __init__(self, value, prev, next=None) -> None:
        self.value = value
        self.prev = prev
        self.next = next
    
    def insertAfter(self, value):
        temp = self.next
        self.next = Node(value, self, temp)
        temp.prev = self.next

class LinkedList:
    def __init__(self, list) -> None:
        self.length = 0
        self.start = None
        self.last = None
        for v in list:
            self.append(v)
    
    def append(self, value):
        if self.last:
            self.last.next = Node(value, self.last)
            self.last = self.last.next
        else:
            self.start = Node(value, None)
            self.last = self.start
    
    def loop(self, func, reverse=False):
        current = self.last if reverse else self.start
        index = 0
        if (reverse):
            print(f"{current.prev.value} <- {current.value} -> {current.next}")
        while current:
            func(index, current.value, current)
            current = current.prev if reverse else current.next
            index += 1
    
    def __repr__(self) -> str:
        s = ''
        def appendString(index, value, node):
            nonlocal s
            s += value
        
        self.loop(appendString)

        return s

def getRulesFromInput(input):
    rules = {}
    for line in input:
        s = line.split(' -> ')
        rules[s[0]] = s[1]
    return rules

def polymerize(index, value, node):
    # print(node.next)
    if node.next:
        newValue = rules[f"{value}{node.next.value}"]
        if newValue:
            node.insertAfter(newValue)

def findCommon(polymerChain: LinkedList):
    counts = {}

    def count(index, value, node):
        nonlocal counts
        count = counts.get(value, 0)
        count += 1
        counts[value] = count
    
    polymerChain.loop(count)

    min = None
    max = None

    for k, v in counts.items():
        if min == None or v < min:
            min = v
        if max == None or v > max:
            max = v

    return (min, max)
        
input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

polymerChain = LinkedList(input[0])

rules = getRulesFromInput(input[2:])

for k, v in rules.items():
    print(f"{k}->{v}")

polymerChain.loop(lambda i, v, n: print(v))

for i in range(10):
    polymerChain.loop(polymerize, True)

minMax = findCommon(polymerChain)

print(minMax[1] - minMax[0])
