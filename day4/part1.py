import os
import re

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

def parseBoardsFromInput(input):
    boards = []

    boardIndex = 0

    for i in range(len(input)):
        if (i >= 2 and len(input[i]) > 10):
            if (len(boards) == boardIndex):
                boards.append([])
            # split and convert each string to int
            boardNumbers = [[int(i), False] for i in re.split('\s+', input[i].strip())]
            boards[boardIndex].append(boardNumbers)
            if (len(boards[boardIndex]) == 5):
                boardIndex += 1
    
    return boards

def printBoard(board):
    for line in board: print(line)

def playNumber(board, num):
    for y in range(len(board)):
        line = board[y]
        for x in range(len(line)):
            if line[x][0] == num:
                line[x][1] = True

def areAllItemsMatched(list):
    for n in list:
        if not n[1]:
            return False
    
    return True

def findWinningBoard(boards):
    for board in boards:
        for i in range(len(board)):

            #horizontal
            if areAllItemsMatched(board[i]):
                return board
            
            #vertical
            verticalMatch = True
            for y in range(len(board)):
                if not board[y][i][1]:
                    verticalMatch = False
            if verticalMatch:
                return board
    
    return None
            
def findSumOfUnmarked(board):
    sum = 0
    for line in board:
        for n in line:
            if n[1] == False:
                sum += n[0]
    return sum

###### BEGIN ######

numbers = [int(i) for i in input[0].split(',')]
boards = parseBoardsFromInput(input)

for num in numbers:
    for board in boards:
        playNumber(board, num)

    winningBoard = findWinningBoard(boards)

    if winningBoard:
        sum = findSumOfUnmarked(winningBoard)

        print("winning board:")
        printBoard(winningBoard)
        print(f"winning number: {num}")
        print(f"sum: {sum}")
        print(f"answer: {num * sum}")
        break