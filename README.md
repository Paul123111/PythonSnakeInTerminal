# PythonSnakeInTerminal
This program allows the user to play the game 'Snake' on a terminal interface. Simply create a file with the code from TerminalSnake.py in this repository and execute in a terminal to play Snake.

# Controls and Instructions
WASD to move
Q to end the program

ASCII symbols:
'@' - snake head
'O' - snake body
'.' - empty space
'a' - apple
'|', '*', '_' - walls

# Arguments
The user can optionally use the '--size' argument with three more arguments to choose the width and height of the grid, and the number of apples on the screen at once.

Example: python3 TerminalSnake.py --size 64 32 5
Creates a 64x32 grid with 5 apples on screen at once.

# Requirements
Works on Ubuntu Linux 24.04
Requires module 'curtsies' to be installed in the user's python environment.
