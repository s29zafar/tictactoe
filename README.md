# Undefeatable TIC TAC TOE
The program is a Dynamic program, that uses a game theory mechanism to implement a AI-like tic-tac-toe player.

The game has three players, specified in player.py:

1) Human player: aka the user. The mechanism to see input and output is mentioned in class TicTacToe in game.py.

2) Random Computer Player: Chooses any random integer between 0-9, which is not yet selected and returns it.

3) Genius Computer Player: Uses the minimax simulation to run through all the possible outcomes of every possible input and finds the best move.


The game.py implements the game. It prints the board, starts the game, makes moves, initiates the game board and checks for winners. An example of this is in the following image:

<img width="258" alt="Screenshot 2023-07-24 at 4 41 41 PM" src="https://github.com/s29zafar/tictactoe/assets/69566994/f34a3e20-7184-47f3-8866-00fb8f880d9b">

### We see that the X player wins. 


The gameAI.py does the same things as game.py but uses the Genius Computer Player instead of the Random Computer Player. An example of this is in the following image:

<img width="400" alt="Screenshot 2023-07-24 at 4 33 22 PM" src="https://github.com/s29zafar/tictactoe/assets/69566994/3aedf287-b63c-42b5-b056-3a0f20c96622">

### We see that the game is tied. This is always consistent with the mini-max algorithm as it will either win or tie, but never lose. 

The program uses Object Oriented Programming to work around the three algorithms. 

# Hope you like the game :)
