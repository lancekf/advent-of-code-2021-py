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
    print("")

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

def isBoardAWinner(board):
    for i in range(len(board)):

        #horizontal
        if areAllItemsMatched(board[i]):
            return True
        
        #vertical
        verticalMatch = True
        for y in range(len(board)):
            if not board[y][i][1]:
                verticalMatch = False
        if verticalMatch:
            return True
    
    return False
            
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

lastWinningBoardIndex = None

for num in numbers:
    print(f"playing number: {num}")
    for i in range(len(boards)):
        board = boards[i]
        if board != None:
            playNumber(board, num)
            if isBoardAWinner(board):
                lastWinningBoardIndex = i
                boards[i] = None
                print(f"latest winner: {lastWinningBoardIndex} with num: {num}")

# replay up until the last winner wins
boards = parseBoardsFromInput(input)
for num in numbers:
    board = boards[lastWinningBoardIndex]
    playNumber(board, num)
    
    if isBoardAWinner(board):
        sum = findSumOfUnmarked(board)

        print("winning board:")
        printBoard(board)
        print(f"winning number: {num}")
        print(f"sum: {sum}")
        print(f"answer: {num * sum}")
        break