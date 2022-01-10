from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:

    def __init__(self):
        self.board = [' ' for x in range(9)]
        self.current_winner = None

    # print_board() prints the board
    # effects: produces output
    # time: O(n) n is the size of board
    # note: must be used after every move
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + "|".join(row) + " |")

    # print_board_nums() prints the reference boards
    # effects: produces output
    # time: O(n) n is the size of board
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + "|".join(row) + " |")

    # available_moves() find all the available moves
    # effects: stores data in moves and returns it
    # time: O(n) n is the size of board
    # note: available moves are square with " " in them
    def available_moves(self):
        moves = []
        for (i,spot) in enumerate(self.board):
            # ['x','x','o'] --> [(0,'x'),(1,'x'),(2,'o')]
            if spot == " ":
                moves.append(i)
        return moves

    # empty_squares() checks if there are empty squares in object(board)
    # time: O(n) n is the size of board
    def empty_squares(self):
        return " " in self.board

    # num_empty_squares() returns the length of available_moves in board
    # time: O(n) n is the size of board
    def num_empty_squares():
        return len(available_moves())

    # make_move(square, letter) changes the board at square with letter
    # effects: changes the object(board and current_winner)
    # time: O(n) n is the size of board
    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else :
            return False

    # winner(square, letter) checks if the row, column and diagonals at square
    #   is equal to letter and returns True else False
    def winner(self, square, letter):
        # check rows
        row_index = square // 3
        row = self.board[row_index*3 : (row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # check columns
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

# play(game, x_player, o_player, print_game) plays the game of TicTacToe in game
# effects: Takes Input, produces Output and 
# time: O(n), where n is the size of board
def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = "X" # the starting letter

    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print("")
            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            letter = "O" if letter == "X" else "X"

    if print_game:
        print("It\'s a tie!")

if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)
