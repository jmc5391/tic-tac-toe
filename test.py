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

    def change_square(self, choice, player):
        if player == 1:
            self.squares[int(choice)] = 'X'
        else:
            self.squares[int(choice)] = 'O'

board = Board()
board.draw_board()
board.get_input(1)
board.draw_board()
board.get_input(1)
board.draw_board()
board.get_input(1)
board.draw_board()