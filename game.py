#**************************************************************************************************
# Created by Carrik McNerlin
# May 5, 2021
#
# This file holds all the game logic for an instance of the Minesweeper game.
#**************************************************************************************************
from boardFunctions import *

# Create an instance of the game
def play(board_size, num_mines):
    #**********************************************************************************************
    # I used a variable for this when I recognized how many times this character is referenced.
    # If I were to decide instead to use another character to signify bombs,
    # it would take forever to replace otherwise.
    #**********************************************************************************************
    bomb_char = 'B'
    
    hidden = createHiddenBoard(board_size, num_mines, bomb_char)
    player = createPlayBoard(board_size)
    win = True # Defined before we enter the loop
    
    # show initial board of '-'s
    printBoard(player, board_size)
    
    # Continue until the board is fully discovered except for mines
    guesses = 0
    previous_guesses = []
    while (guesses < (board_size**2 - num_mines)):
                
        # default to out of range to guarantee getting input
        x = 0
        y = 0
        
        while (x < 1 or x > board_size) or (y < 1 or y > board_size):
            x = int(input("Enter an x value:"))
            y = int(input("Enter a y value:"))
            
            if (x < 1 or x > board_size) or (y < 1 or y > board_size):
                print("Can't choose a position off the board.")
            
            curr_guess = [x,y]
            
            if curr_guess in previous_guesses:
                print("You've already chosen this space.")
            
            previous_guesses.append(curr_guess)
        # end spot selection loop
            
        guesses += 1
        # Change inputs to 1 less than desired because indexing starts at 0.
        x -= 1
        y -= 1
        
        
        
        # Replace the character at y,x in user board with info from hidden board
        player = revealHidden(x, y, hidden, player)
        
        # Show the current board-state.
        printBoard(player, board_size)
        
        # The player loses if they chose a place with a bomb.
        if player[y][x] == bomb_char:
            win = False
            break
        
    # end guessing loop  
        
    printBoard(hidden, board_size)
    if win == True:
        print("Congratulations! You won!")
    else:
        print("Better luck next time.")

# end play()
