# Day 4: Giant Squid
#!/usr/bin/python

def prettyPrintBoard(board):
    for line in board:  
        print(line)

def prettyPrintBoards(boards):
    for board in boards:
        for line in board:
            print(line)
        print()

def markNumber(boards,number):
    for b, board in enumerate(boards):
        for l, line in enumerate(board):
            if number in line:
                for v,value in enumerate(line):
                    if(value == number):
                        boards[b][l][v] = -1

def checkForBingoHorizontal(boards,boardWins):
    #check horizontals
    victoryBoards = []
    for b, board in enumerate(boards):
        if(boardWins[b]):
            continue
        horizontalBingo = False;
        for l, line in enumerate(board):
            if(line.count(-1) == 5):
                horizontalBingo = True
                break
        
        if(horizontalBingo):
            print("Horizontal Board win on: ", b+1)
            prettyPrintBoard(board)
            boardWins[b] = True
            victoryBoards.append(b)

    if(victoryBoards != []):
        return victoryBoards
    else:
        return -1

def checkForBingoVertical(boards,boardWins):  
    # check vertical
    victoryBoards = []
    for b, board in enumerate(boards): 
        if(boardWins[b]):
            continue
        verticalBingo = False;
        columns = []
        for x in range(5):
            column = []
            for y in range(5):
                column.append(board[y][x])
            if (column.count(-1) == 5):
                 verticalBingo = True
                 break   

        if(verticalBingo):
            print("Vertical Board win on: ", b+1)
            boardWins[b] = True
            prettyPrintBoard(board)
            victoryBoards.append(b)

    if(victoryBoards != []):
        return victoryBoards
    else:
        return -1

def checkForBingo(boards,boardWins):
    horizontalVictory = checkForBingoHorizontal(boards,boardWins)
    verticalVictory = checkForBingoVertical(boards,boardWins) 

    if(horizontalVictory != []):
        return horizontalVictory
    elif(verticalVictory != []):
        return verticalVictory
    else:
        return -1

def getSumOfBoard(board):
    boardSum = 0;
    for line in board: 
        for value in line: 
            if(value != -1):
                boardSum += value;
    
    return boardSum;


# Part 1

input = open('input.txt','r')

firstLine = input.readline().strip().split(",")
randomNumbers = [int(i) for i in firstLine]

print("Random numbers: ", randomNumbers)

boards = []


for line in input:
    if line not in ['\n', '\r\n']:
        values = list(map(int,line.strip().split()))
        boards[-1].append(values)
    else:
        # add new board
        boards.append([])

boardWins =  [False for i in range(len(boards))]

for number in randomNumbers:
    # mark numbers
    markNumber(boards,number)
    checkValue = checkForBingo(boards,boardWins)
    if(boardWins.count(True) == len(boardWins)):
        print(checkValue)
        print("Number: ",number)
        if(checkValue != []):
            sumOfBoard = getSumOfBoard(boards[checkValue[0]])
            print("Final Score: ", sumOfBoard * number)
        break;
        
