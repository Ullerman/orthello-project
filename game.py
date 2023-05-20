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




class OthelloGame:
    def __init__(self):
        self.board = [
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "B", "W", "-", "-", "-"],
            ["-", "-", "-", "W", "B", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"]
        ]
        self.player = 'B'

    def display_board(self):
        print("         ", end="")
        for col in range(1, 9):
            print(col, end="    ")
        print("\n     +-------------------------------------------+")
        for row in range(len(self.board)):
            print(row + 1, end="    |   ")
            for cell in self.board[row]:
                print(cell, end="    ")
            print("|\n     |                                           |")
        print("     +-------------------------------------------+")
    def can_flip_pieces(self,row,col,direction):
        piece_colour = self.board[row][col]
        if direction == "down" and self.board[row][col+1] != piece_colour:
            for i in range(col, 8):
                if self.board[row][col+1] != piece_colour:
                    valid_move = False
                else:
                    valid_move = True
            if valid_move == True:
                takenpieces = [[row,j] for j in range(col,i)]
                for r , c in takenpieces:
                    self.board[r][c] = self.player
        elif direction == "up" and self.board[row][col+1] != piece_colour:
            for i in range(0,col):
                if self.board[row][col-1] != piece_colour:
                    valid_move = False
                else:
                    valid_move = True
            if valid_move == True:
                takenpieces = [[row,j] for j in range(col,i)]
                for r , c in takenpieces:
                    self.board[r][c] = self.player
        


            

                
                    
            


    def make_move(self, row, col):
        if self.board[row][col] != "-":
            print(f"There is already a piece there belonging to {self.board[row][col]}.\nInvalid move.")
            return False
    

    def is_game_over(self):
        # Implement the logic to check if the game is over
        pass

    def calculate_winner(self):
        # Implement the logic to calculate the winner of the game
        pass

    def play(self):
        game_over = False

        while not game_over:
            self.display_board()

            row = int(input("Enter the row number: "))
            col = int(input("Enter the column number: "))

            self.make_move(row - 1, col - 1)

            if self.is_game_over():
                game_over = True
                self.display_board()
                print("Game over!")
                winner = self.calculate_winner()
                if winner == 'B':
                    print("Black (B) wins!")
                elif winner == 'W':
                    print("White (W) wins!")
                else:
                    print("It's a draw!")

# Create an instance of the OthelloGame class
game = OthelloGame()
# Start the game
game.play()
