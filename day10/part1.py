import os

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

openBrackets = [
    '(',
    '[',
    '{',
    '<'
]

closingBrackets = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
    }

def findIllegalCharacter(line):
    stack = []
    for c in line:
        if c in openBrackets:
            stack.append(c)
        else:
            openBracket = closingBrackets[c]
            lastBracket = stack.pop()
            if openBracket != lastBracket:
                return c

illegalLines = []
for line in input:
    illegalChar = findIllegalCharacter(line)
    if illegalChar:
        print(f"{illegalChar} in {line}")
        illegalLines.append((line, illegalChar))
                
scorecard = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
    }

score = 0
for line in illegalLines:
    score += scorecard[line[1]]

print(score)