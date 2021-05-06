#**************************************************************************************************
# Created by Carrik McNerlin
# May 5, 2021
#
# This is the driver application for playing Minesweeper on an MxM grid with N mines.
# Each game uses 2 boards, one to show the player and one that holds the mines and proximity count.
# When the player chooses a space, swap the character with the one at that square on the mine board.
#**************************************************************************************************

from game import * #game imports boardFunctions.py

# default to yes for initial playthrough
keep_playing = 'y'

while (keep_playing[0].lower() == 'y'):
    board_size = int(input("How many rows and columns would you like the board to be?\n"))

    num_mines = board_size**2 + 1
    # can't have more mines than spaces
    while (num_mines > board_size**2):
        num_mines = int(input("How many mines would you like there to be?\n"))
        
    play(board_size,num_mines)
        
    keep_playing = str(input("Would you like to play again?\n"))
#end while