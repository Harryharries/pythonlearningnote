import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#####

# function: generateInit

# - Initalize the simulation, It will return a np 2d array board

# - paramter:

#       int: boardSize - the square playground Size

#       double: density - the density can control the random event happen in the simulation

# - return:

#       2d array: newBoard - the 2D array which can be showed in animation

#####
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

#####

# function: countNeighbours

# - Conut how many Neighbours around the cell [row,col] and Automatically detacted the boundary 

# - paramter:

#       2d array: board - the current board

#       int: row - the cell is row number

#       int: col - the cell is collom number

# - return:

#       int: num - how many Neighbours around the cell[row,col]

#####
def countNeighbours(board, r, c):
    global boardSize
    num = 0
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            #Automatically detacted the boundary
            if((not(i==r and j == c)) and (not(i<0 or i >= boardSize)) and(not (j >= boardSize or j<0)) and (board[i][j])):
                num+=1
    return num

#####

# function: updateNext

# - update(return) a new 2d array which decided by last generation

# - paramter:

#       2d array: board - the current board

# - return:

#       2d array: newBoard - new 2d array which decided by last generation

#####
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

#####

# function: update

# next animation set up

#####
def update(data):
    global myb
    newb = updateNext(myb)
    mat.set_data(newb)
    myb = newb
    return [mat]


# the density can control the random event happen in the simulation

density = 0.1

#the square playground Size

boardSize = 30

#the number of generation in the simulation

numberOfGen = 10

#Initalization

myBoard =  generateInit(density,boardSize)

#set the original board

myBoard[1,1] = 1

myBoard[3,1] = 1

myBoard[1,4] = 1

myBoard[2,5] = 1

myBoard[3,5] = 1

myBoard[4,5] = 1

myBoard[4,4] = 1

myBoard[4,3] = 1

myBoard[4,2] = 1

#animation set up

fig, ax = plt.subplots()

mat = ax.matshow(myBoard)

ani = animation.FuncAnimation(fig, update, interval=10,save_count=250)

plt.show()