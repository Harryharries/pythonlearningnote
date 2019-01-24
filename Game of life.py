import numpy as np
import random

density = 0.1
boardSize = 30
numberOfGen = 10

def generateInit(density,boardSize):
    board = []
    for i in range(boardSize):
        board.append([])
        for j in range(boardSize):
            c = 0
            if random.randint(0,100)  < density*100:
                c = 1
            board[i].append(c)
    b = np.array(board)
    return  b

def countNeighbours(board, r, c):
    global boardSize
    num = 0
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            if((not(i==r and j == c)) and (not(i<0 or i >= boardSize)) and(not (j >= boardSize or j<0)) and (board[i][j])):
                num+=1
    return num

def updateNext(board):
    newBoard = board.copy()
    for i in range(boardSize):
        for j in range(boardSize):
            if (board[i][j]):
                if(countNeighbours(board,i,j)==2 or countNeighbours(board,i,j)==3):
                    newBoard[i][j]=1
                else:
                    newBoard[i][j] = 0
            else:
                if(countNeighbours(board,i,j)==3):
                    newBoard[i][j] = 1
                else:
                    newBoard[i][j]=0
    return newBoard

def printGeneration(board):
    global numberOfGen
    newboard = board.copy()
    print("generation: 0")
    print(newboard)
    for i in range(0,numberOfGen):
        r = i+1
        print("\n\n")
        print("generation: "+str(r))
        newboard = updateNext(newboard)
        print(newboard)





myb =  generateInit(density,boardSize)
printGeneration(myb)