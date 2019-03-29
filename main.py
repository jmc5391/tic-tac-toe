class Board:
    def __init__(self):
        #class begins with dictionary representing the nine squares of board
        #squares begin with value '1-9' so player can choose them with input
        self.squares = {
            1: '1', 
            2: '2', 
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9'}

    def draw_board(self):
        #method for board to print itself including dividers
        #uses string concatenation
        print(" " + self.squares[1] + " | " + self.squares[2] + " | " + self.squares[3])
        print("---+---+---")
        print(" " + self.squares[4] + " | " + self.squares[5] + " | " + self.squares[6])
        print("---+---+---")
        print(" " + self.squares[7] + " | " + self.squares[8] + " | " + self.squares[9])

    def square_is_taken(self, choice):
        #checks if square already has an X or O in it
        square_contents = self.squares[int(choice)]
        if square_contents.isnumeric() == False:
            print("Oops, that square is already taken! Try again.")
            return True
        else:
            return False

    def is_valid_input(self, choice):
        #checks if input is number between 1 and 9
        if choice.isnumeric():
            if int(choice) < 10 and int(choice) > 0:
                return True
        print("Oops, enter a number between 1 and 9")
        return False
            
    def get_input(self, player):
        #gets input from player and verifies valid input before changing square value
        choice = input("Player " + str(player) + ", pick a square. (1-9)\n>")
        if self.is_valid_input(choice):
            if self.square_is_taken(choice) == False:
                self.change_square(choice, player)
            else:
                self.get_input(player)
        else:
            self.get_input(player)

    def change_square(self, choice, player):
        if player == 1:
            self.squares[int(choice)] = 'X'
        else:
            self.squares[int(choice)] = 'O'

    #method for board to reset itself

    #method to check if a player has won
    def has_won(self):
        #check horizontal lines
        for i in range(1, 10, 3):
            if self.squares[i] == self.squares[i+1] and self.squares[i+1] == self.squares[i+2]:
                return True
        #check vertical lines
        for i in range(1, 4):
            if self.squares[i] == self.squares[i+3] and self.squares[i+3] == self.squares[i+6]:
                return True
        #check diagonal lines
        if self.squares[1] == self.squares[5] and self.squares[1] == self.squares[9]:
            return True
        if self.squares[3] == self.squares[5] and self.squares[3] == self.squares[7]:
            return True
        return False

    #method to check if there is a draw
    def is_draw(self):
        #check horizontal rows
        for i in range(1, 10, 3):
            sample_string = self.squares[i] + self.squares[i+1] + self.squares[i+2]
            #if the row is clear of player symbols, there's no draw yet
            if self.squares[i].isnumeric() and self.squares[i+1].isnumeric() and self.squares[i+2].isnumeric():
                return False
            #if only one player has gone in the row, there's no draw yet
            elif 'X' in sample_string and 'O' not in sample_string:
                return False
            elif 'O' in sample_string and 'X' not in sample_string:
                return False
        #check vertical lines
        for i in range(1, 4):
            sample_string = self.squares[i] + self.squares[i+3] + self.squares[i+6]
            #if the row is clear of player symbols, there's no draw yet
            if self.squares[i].isnumeric() and self.squares[i+3].isnumeric() and self.squares[i+6].isnumeric():
                return False
            #if only one player has gone in the row, there's no draw yet
            elif 'X' in sample_string and 'O' not in sample_string:
                return False
            elif 'O' in sample_string and 'X' not in sample_string:
                return False
        #check diagonal lines
        #if the row is clear of player symbols, there's no draw yet
        diag1 = self.squares[1] + self.squares[5] + self.squares[9]
        diag2 = self.squares[3] + self.squares[5] + self.squares[7]
        if self.squares[1].isnumeric() and self.squares[5].isnumeric() and self.squares[9].isnumeric():
            return False
        if self.squares[3].isnumeric() and self.squares[5].isnumeric() and self.squares[7].isnumeric():
            return False
        #if only one player has gone in the row, there's no draw yet
        if 'X' in diag1 and 'O' not in diag1:
            return False
        if 'O' in diag1 and 'X' not in diag1:
            return False
        if 'X' in diag2 and 'O' not in diag2:
            return False
        if 'O' in diag2 and 'X' not in diag2:
            return False
        #if none of these checks return False, there's a draw and the method returns True
        return True

    def draw(self):
        self.draw_board()
        print("It's a draw!")

    def play_again():
        answer = input("Would you like to play again?(Y/N)")
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            return True
        else:
            return False

def intro():
    #ran once when game is first started
    #welcome player
    print("Welcome to Tic-Tac-Toe!")
    #explain rules
    print("Player 1 is X's, Player 2 is 0's.")
    print("Pick a square to draw your symbol in and try to get three in a row!")


    #check if still possible for anyone to win
    #returns boolean

#def play_again():
    #ask if player wants to play again
    #returns boolean

def game(board):
    #loop:
    while True:
        #loops between player 1 and 2
        for player in range(1,3):
            #draw the board
            board.draw_board()
            #current player picks a square
            board.get_input(player)
            #check if current player has won:
            if board.has_won():
                #if so, tell player and end function
                board.draw_board()
                print("Player " + str(player) + " has won!")
                return player
            #if not, check if draw:
            elif board.is_draw():
                board.draw()
                return 0
            #if neither loop continues to player until either condition met

def main():
    #create the board object
    board = Board()
    #welcome the player
    intro()
    #loop:
    #while True:
        #start the game loop
    game(board)
        #ask player if wants to play again:
        #if not board.play_again():
            #if not, break the loop
            #break

if __name__ == '__main__':
    main()