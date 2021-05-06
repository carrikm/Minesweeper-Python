#**************************************************************************************************
# Created by Carrik McNerlin
# May 5, 2021
#
# This file holds all the game logic for an instance of the Minesweeper game.
#**************************************************************************************************
from boardFunctions import *

# Create an instance of the game
def play(board_size, mines):
    #**********************************************************************************************
    # I used a variable for this when I recognized how many times this character is referenced.
    # If I were to decide instead to use another character to signify bombs,
    # it would take forever to replace otherwise.
    #**********************************************************************************************
    bomb_char = 'B'
    
    hidden = createHiddenBoard(board_size, mines, bomb_char)
    player = createPlayBoard(board_size)
    win = True # Defined before we enter the loop
    
    #show initial board of '-'s
    printBoard(player, board_size)
    
    #continue until 
    while (player != hidden):
                
        # Change inputs to 1 less than desire because indexing starts at 0.
        x = int(input("Enter an x value:"))
        y = int(input("Enter a y value:"))
        x -= 1
        y -= 1
        
        # Replace the character at y,x in user board with info from hidden board
        player = revealHidden(x, y, hidden, player)
        
        # Show the current board-state.
        printBoard(player, board_size)
        
        # The player loses if they chose a place with a bomb.
        if player[y][x] == bomb_char:
            win = False
            printBoard(hidden, board_size)
            break
        
        

    if win == True:
        print("Congratulations! You won!")
    else:
        print("Better luck next time.")

#end play()