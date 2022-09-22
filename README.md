# Undefeatable TIC TAC TOE
The program is a Dynamic program, that uses a game theory mechanism to implement a AI like tic-tac-toe player.

The game has three player, specified in player.py:

1) Human player: aka the user. Mechanism to see input and output is mentioned in class TicTacToe in game.py.

2) Random Computer Player: Chooses any random integer between 0-9, which is not yet selected and return it.

3) Genius Computer Player: Uses the minimax simulation to run through all the possible outcomes of every possible input and finds the best move.


The game.py implements the game. It prints the board, starts the game, makes moves, initiates game board and checks for winners. 

The gameAI.py does the same things as game.py but uses the Genius Computer Player instead of the Random Computer Player.

The program uses Object Oriented Programming to work around the three algorithms. 

# Hope you like the game :)
