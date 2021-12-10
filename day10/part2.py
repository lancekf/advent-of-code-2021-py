import os

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

openBrackets = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}

closingBrackets = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
    }

def findValidLines(line):
    stack = []
    for c in line:
        if c in openBrackets:
            stack.append(c)
        else:
            openBracket = closingBrackets[c]
            lastBracket = stack.pop()
            if openBracket != lastBracket:
                return None
    
    return stack

def getAutoCompletion(line, stack):
    autoCompletion = []

    while stack:
        bracket = stack.pop()
        if bracket in openBrackets:
            autoCompletion.append(openBrackets[bracket])
        else:
            raise Exception(f'Found invalid bracket in stack! {bracket} at char {len(stack)}')
    
    return autoCompletion

autoCompletes = []
for line in input:
    stack = findValidLines(line)
    if stack:
        print(f"Incomplete: {line}")
        autoCompletion = "".join(getAutoCompletion(line, stack))
        autoCompletes.append(autoCompletion)
        print(autoCompletion)
                
scorecard = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
    }


scores = []
for line in autoCompletes:
    score = 0
    for bracket in line:
        score = score * 5 + scorecard[bracket]
    print(f"{line}: {score}")
    scores.append(score)

scores = sorted(scores)
index = int((len(scores)-1) / 2)
print(scores[index])