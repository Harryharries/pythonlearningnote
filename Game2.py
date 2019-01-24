import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


density = 0.1
boardSize = 30
numberOfGen = 10


def generateInit(density,boardSize):
    board = []
    for i in range(boardSize):
        board.append([])
        for j in range(boardSize):
            c = 0
            # if random.randint(0,100)  < density*100:
            #     c = 1
            board[i].append(c)
    b = np.array(board)
    return  b


myb =  generateInit(density,boardSize)
myb[1,1] = 1
myb[3,1] = 1
myb[1,4] = 1
myb[2,5] = 1
myb[3,5] = 1
myb[4,5] = 1
myb[4,4] = 1
myb[4,3] = 1
myb[4,2] = 1


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

def update(data):
    global myb
    newb = updateNext(myb)
    mat.set_data(newb)
    myb = newb
    return [mat]




fig, ax = plt.subplots()
mat = ax.matshow(myb)
ani = animation.FuncAnimation(fig, update, interval=10,
                              save_count=250)
plt.show()