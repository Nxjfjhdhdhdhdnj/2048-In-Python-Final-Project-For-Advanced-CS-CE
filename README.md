2048 Game
This is a Python implementation of the popular game 2048. The game is played on a 4x4 grid, where the player combines tiles with the same number to achieve the goal of reaching 2048.

How to Play
Run the Python script 2048_game.py to start the game.
The initial game grid will be displayed on the console.
Use the following keys to make moves:
W or w: Move tiles upwards.
S or s: Move tiles downwards.
A or a: Move tiles to the left.
D or d: Move tiles to the right.
After each move, the updated game grid will be displayed.
Continue making moves until you reach the goal of 2048 or there are no valid moves left.
If you reach 2048, you win the game!
You can choose to continue playing or stop the game.
Bugs and Known Issues
Random number generator overlaps two numbers on a tile or only generates one tile at the beginning of each game. (Status: Fixed)
Bug where the numbers will add to each repeatedly in the input process. (Status: Maybe fixed with q >= 4 in the inputProcessing function)
Bug where the array will repeatedly generate random numbers despite there being no movement. (Status: Fixed)
The game stops processing inputs when there are no 0's in the array. (Status: Maybe fixed, but still occurs when numbers are randomly generated)
Please note that this README file mentions some known bugs and their current status. If you encounter any issues or have suggestions for improvements, please feel free to contribute to the code or report the problems.

Enjoy playing the 2048 game!
