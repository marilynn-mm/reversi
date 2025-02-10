# Project Description

We simulated the board game Reversi through Python. The game takes place on a 8x8 board with player one being X and player two being O. Each turn, players must capture some of their opponent's pieces by making a play that sandwiches the opponent's piece(s) between their own. 

When a piece(s) is captured, they are flipped to the opponent's symbol i.e. if player one places an X in the blank, player two's O's will turn into into X's XOOO_ --> XOOOX -> XXXXX

The game is then played until the board is full and the winner will be determined once the board is full. Players will have the option of choosing between three game-modes: human vs human match, human vs AI match, and AI vs AI match.

## Various Versions of the Game: 

### Human vs. Human Mode (hostGame): 
Two human players engage in a game of Reversi. Players take turns placing their pieces ('X' and 'O') on the board, with 'X' always going first. Each player selects a row and column for their move using the input function.

### Human vs. Random AI Mode (hostRAIGame)
A human player faces off against an AI opponent that plays randomly. Similar to the Human vs. Human mode, players take turns placing their pieces on the board, with 'X' going first. The AI's moves are determined randomly given a list of moves available by the function listOfMoves and randomAIMove.

### AI vs. AI Mode (host2AIGame)
Two AI opponents face each other in a game of Reverse. Both AIs play at ply 1 - more description below, taking turns to make moves on the board.

### Human vs. Smart AI Mode (hostSmartAIGame)
A human player competes against a smart AI opponent. Similar to previous modes, players take turns placing their pieces on the board, with 'X' going first. The AI opponent employs smart strategies to make informed moves. First it assesses the scores — number of pieces that will be captured in a move — of all possible moves, identifies the move will the maximum score, and implements that move.

## User Interface:

Each run of the program begins by welcoming the player to the game and creating an 8x8 board which is in accordance with normal Reversi rules. The board is set up with four central squares of the board alternating ‘X’s and ‘O’s.

In the modes with human players (player v player, player v random AI, player v smart AI), we collect user input by first asking the row they’d like to play in and then the column. 

After each move, we print a tally of how many pieces each player has, print the board, and prompt the next player/AI to make the following move.

Once the board is full, the game ends with an announcement of the winner, a tally of ‘X’ and ‘O’ pieces respectively, and the difference between the two. Then, it prompts the user to restart a game.

## Results & Reflections:

Overall, Reversi was very fun to work on as it was a game we both knew well. Our most difficult challenge was laying the foundation for our pieces to flip in all 8 directions (in our code, this refers to the check and flip functions).

With more time, we would’ve liked to create a ply 2 for our smart AI and experiment with creating a Misère AI. In the end, we were happy with how our game ran, especially the fact that our user has a variety of well-functioning modes to choose from.
