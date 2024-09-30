# Snake In Terminal
This program allows the user to play the game 'Snake' on a terminal interface. <br>
Simply create a file with the code from TerminalSnake.py in this repository and execute this file in a terminal to play Snake.

# Controls and Instructions
WASD to move <br>
Q to end the program

ASCII symbols: <br>
- '@' - snake head <br>
- 'O' - snake body <br>
- '.' - empty space <br>
- 'a' - apple <br>
- '|', '*', '_' - walls <br>

# Arguments
The user can optionally use the '--size' argument with three more arguments to choose the width and height of the grid, and the number of apples on the screen at once. Without this argument, the game will default to a 32x32 grid with 1 apple.

Example: python3 TerminalSnake.py --size 64 32 5 <br>
Creates a 64x32 grid with 5 apples on screen at once.

# Requirements
- Works on Ubuntu Linux 24.04 <br>
- Requires module 'curtsies' to be installed in the user's python environment.
- Make sure the grid size can fit on the terminal screen
