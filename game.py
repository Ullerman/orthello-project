"""
In Othello (also known as Reversi), the rules for making a move are as follows:

The game is played on an 8x8 grid board, initially empty except for the center four cells.

Each player starts with two pieces of their color (black 'B' and white 'W') placed diagonally in the center of the board.

Players take turns making moves. Black always moves first.

To make a valid move, a player must place their piece in an empty cell such that it encloses one or more of the opponent's pieces between their newly placed piece and any of their own pieces already on the board.

The player making the move must place their piece in a position that allows for the capture of at least one opponent's piece. This capture is achieved by sandwiching one or more of the opponent's pieces between two pieces of the player's own color in a horizontal, vertical, or diagonal line.

After placing the new piece, all opponent's pieces that are sandwiched between the newly placed piece and any existing pieces of the player's color are flipped, changing their color to the player's color.

If a player cannot make a valid move, their turn is skipped, and the other player continues to make moves. If neither player can make a valid move, the game ends.

The game ends when the board is full or when no more valid moves can be made. The player with the most pieces of their color on the board at the end of the game is the winner.

These are the basic rules for making moves in Othello. Implementing these rules in your code will allow players to take turns, validate moves, update the board, and determine the winner of the game."""

Board = [
# 1   2   3   4   5   6   7   8
["-","-","-","-","-","-","-","-",],
["-","-","-","-","-","-","-","-",],
["-","-","-","-","-","-","-","-",],
["-","-","-","B","W","-","-","-",],
["-","-","-","W","B","-","-","-",],
["-","-","-","-","-","-","-","-",],
["-","-","-","-","-","-","-","-",],
["-","-","-","-","-","-","-","-",]
]

def display_board():
    # Print column labels
    print("         ", end="")
    for col in range(1,9):
        print(col, end="    ")
    print("\n     +-------------------------------------------+")

    # Print rows and cells
    for row in range(len(Board)):
        print(row+1, end="    |   ")
        for cell in Board[row]:
            print(cell, end="    ")
        print("|\n     |                                           |")
    print("     +-------------------------------------------+")


display_board()