# Lab 27: Connect Four

[Connect Four](https://en.wikipedia.org/wiki/Connect_Four) is a board game.
Players take turns placing tokens of their color into a vertical grid.
They drop to the bottom, and if anyone has four of their color in a straight line, they've won!

Define a module that simulates a Connect Four game.

This will consist of the following classes:

`Player`:
- Properties
    - `name`
    - `color`
        
`Game`:
- Properties
    - `board`: 7x6 board representation

- Methods
    - `get_height(position)`: returns int of how many pieces occupy a column 
    - `move(player, position)`: adds a player token to a column after figuring out the current height of the column 
    - `calc_winner()`: returns true if a match (four in a row) is found 
    - `is_full()`: returns true if all board positions are occupied 
    - `is_game_over()`: returns true if the game is over (a winner is found or the board is full)


Create a program that simulates the _just playing moves_ of an existing Connect Four game.
Do not concern yourself with figuring out who has won.

It will read a file that contains a history of the moves in a game.
Assume the playing board is made of columns numbered 1 through 7.
The file will have one line for each move (players alternate).
The number in that line is the column the current player placed a token in.

Use the following [example move file](./connect_four/connect-four-moves.txt).
Save it in something like `connect-four-moves.txt`
This moves file recreates [this game](https://en.wikipedia.org/wiki/File:Connect_Four.gif).

*   Think about how to figure out how far that token will fall in a given column.

*   Think about how to place a token in a column.

*   Think about how to concisely store the tokens that have been dropped in the board.

*   Read in moves from the file.

*   After each move, print out a representation of the board.
    You can use `R` and `Y` to represent the pieces.

## Version 2

*   Once all moves are done, also print out what player, if any, won.

## Version 3

*   Make game playable
