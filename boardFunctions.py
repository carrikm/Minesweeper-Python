#**************************************************************************************************
# Created by Carrik McNerlin
# May 5, 2021
#
# This file contains functions pertaining to the boards.
# That includes creating both the hidden and the user board, printing a board, and revealing spaces.
#**************************************************************************************************
import random

# Mines are placed randomly and the tiles around them are incremented accordingly
def placeMines(board, size, num_mines, bomb_char):
    for num in range(num_mines):
        #add bombs 
        new_space = False
        while new_space == False:
            x = random.randint(0,size-1)
            y = random.randint(0,size-1)
            if board[y][x] != bomb_char:
                new_space = True
            
        board[y][x] = bomb_char
    
        #******************************************************************************************
        # Update count for tiles around the bombs
        #******************************************************************************************
        
        # "if board[y][x] != bomb_char" is in all of these because we don't want to change places that are mines.
    
        # above and left
        if (x >= 1 and x <= size-1) and (y >= 1 and y <= size-1):
            if board[y-1][x-1] != bomb_char:
                board[y-1][x-1] += 1
        
        # directly above
        if (x >= 0 and x <= size-1) and (y >= 1 and y <= size-1):
            if board[y-1][x] != bomb_char:
                board[y-1][x] += 1
        
        # above and right
        if (x >= 0 and x <= size-2) and (y >= 1 and y <= size-1):
            if board[y-1][x+1] != bomb_char:
                board[y-1][x+1] += 1
                
        # directly to the left
        if (x >= 0 and x <= size-1) and (y >= 0 and y <= size-1):
            if board[y][x-1] != bomb_char:
                board[y][x-1] += 1
                
        # directly to the right
        if (x >= 0 and x <= size-2) and (y >=0 and y <= size-1):
            if board[y][x+1] != bomb_char:
                board[y][x+1] += 1         
        
        # bottom left
        if (x >= 1 and x <= size-1) and (y >= 0 and y <=size-2):
            if board[y+1][x-1] != bomb_char:
                board[y+1][x-1] += 1
        
        
        # directly below
        if (x >= 1 and x <= size-1) and (y >=0 and y <= size-2):
            if board[y+1][x] != bomb_char:
                board[y+1][x] += 1
        
        
        # bottom right
        if (x >= 1 and x <= size-2) and (y >= 0 and y <= size-2):
            if board[y+1][x+1] != bomb_char:
                board[y+1][x+1] += 1
    # end for loop
    
    return board
# end placeMines()



# Create a 2-dimensional array of size n where each element is default_char
def initializeBoard(default_char, n):
    return [[default_char for row in range(n)] for col in range(n)]
# end initializeBoard()


# Make the actual board
def createHiddenBoard(size, num_mines, bomb_char):
    #default board of 0s
    board = initializeBoard(0,size)
    placeMines(board, size, num_mines, bomb_char)
    return board
# end createHiddenBoard()



# Create the masked board that the user sees
def createPlayBoard(size):
    #default board has an array of dashes(-)
    board = initializeBoard('-', size)
    return board
# end createPlayBoard()

        
# Replace the character at (y,x) on playBoard with the character from hiddenBoard
def revealHidden(x, y, hiddenBoard, playBoard):
    playBoard[y][x] = hiddenBoard[y][x]
    return playBoard
# end revealHidden()


# Prints the board array that is provided in the form
# [ . . . ]
# [ . . . ]
def printBoard(board, size):
    print('\n')
    for col in range(size):
        print(board[col])
# end printBoard()
        
