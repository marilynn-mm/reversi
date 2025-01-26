Description: 

We will be simulating the board game Reversi or Othello through Python. The game takes place on a 8x8 board with player one being X and player two being O. Each turn, players must capture some of their opponent's pieces by making a play that sandwiches the opponent's piece(s) between their own. 

When a piece(s) is captured, they are flipped to the opponent's symbol i.e. if player one places an X in the blank, player two's O's will turn into into X's XOOO_ --> XOOOX -> XXXXX

The game is then played until the board is full and the winner will be determined once the board is full. Players will have the option of choosing between three game-modes: human vs human match, human vs AI match, and AI vs AI match.

Various Versions of the Game: 

1. Human vs. Human Mode (hostGame): two human players engage in a game of Reversi. Players take turns placing their pieces ('X' and 'O') on the board, with 'X' always going first. Each player selects a row and column for their move using the input function.

2. Human vs. Random AI Mode (hostRAIGame): a human player faces off against an AI opponent that plays randomly. Similar to the Human vs. Human mode, players take turns placing their pieces on the board, with 'X' going first. The AI's moves are determined randomly given a list of moves available by the function listOfMoves and randomAIMove.

3. AI vs. AI Mode (host2AIGame): two AI opponents face each other in a game of Reverse. Both AIs play at ply 1 - more description below, taking turns to make moves on the board.

4. Human vs. Smart AI Mode (hostSmartAIGame): a human player competes against a smart AI opponent. Similar to previous modes, players take turns placing their pieces on the board, with 'X' going first. The AI opponent employs smart strategies to make informed moves. First it assesses the scores — number of pieces that will be captured in a move — of all possible moves, identifies the move will the maximum score, and implements that move.

User Interface:

Each run of the program begins by welcoming the player to the game and creating an 8x8 board which is in accordance with normal Reversi rules. The board is set up with four central squares of the board alternating ‘X’s and ‘O’s.

In the modes with human players (player v player, player v random AI, player v smart AI), we collect user input by first asking the row they’d like to play in and then the column. 

After each move, we print a tally of how many pieces each player has, print the board, and prompt the next player/AI to make the following move.

Once the board is full, the game ends with an announcement of the winner, a tally of ‘X’ and ‘O’ pieces respectively, and the difference between the two. Then, it prompts the user to restart a game.


Progress(milestone stage):

We've been making significant progress with each work session: we successfully coded for each of the 8 directions in which a capture can be made and are currently working on deciding how we'd like our AI to play. Currently, they are all random, but we are thinking of programming them to behave based on ply 1 and Misère rules.


Results & Reflections:

Overall, Reversi was very fun to work on as it was a game we both knew well. Our most difficult challenge was laying the foundation for our pieces to flip in all 8 directions (in our code, this refers to the check and flip functions). By the end, we created 4 game modes:

1. Player vs player
2. Player vs random AI
3. Player vs smart AI
4. Smart AI vs smart AI. 

With more time, we would’ve liked to create a ply 2 for our smart AI and experiment with creating a Misère AI. In the end, we were happy with how our game ran, especially the fact that our user has a variety of well-functioning modes to choose from.



