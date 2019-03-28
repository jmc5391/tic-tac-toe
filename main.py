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

    #def play_again():
        #asks player if they want to play again and returns boolean

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
            #elif board.is_draw():
                #board.draw()
                #break
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