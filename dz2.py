"""
Tic-Tac-Toe game.
"""

import random
import numpy as np

Rows=5
Colls=5


PLAY_BOARD=[]
PLAYERS_MARKS = ['X', 'PC']

for i in range(Rows):
    row = []
    for j in range(Colls):
       row.append(i*Rows + j+1)
    PLAY_BOARD.append(row)

def display_board(board_list):
    """Prints the game board."""
    for row in board_list:
        print(row)

def player_input():
    """Gets player's input string to choose the game mark to play."""
    print('Your marker is X, you play with PC')
    player_first = 'X'
    player_second = 'PC'
    return player_first, player_second

def row_col_number(board,position):
    for i in range(Rows):
        for j in range(Colls):
            if board[i][j]==position:
                return i,j
                break
            
def place_marker(board, marker, position):
    """Puts a player mark to appropriate position."""
    row,col=row_col_number(board,position)
    board[row][col] = marker
                       
def win_check(board, mark, row,col, count):
    """Returns boolean value whether the player wins the game."""
    i,j=row_col_number(board,position)
    print(row,col)
    if (position>1)and(board[row][col]== mark):
            count+=1
    if count == 3:
        return count
    else:
        if position<Rows*Colls:
            win_check(board, mark, i+1,j,count)
            win_check(board, mark, i,j+1,count)
            win_check(board, mark, i+1,j+1,count)
            win_check(board, mark, i-1,j-1,count) 
            win_check(board, mark, i-1,j,count)
            win_check(board, mark, i,j-1,count)
            win_check(board, mark, i-1,j+1,count)
            win_check(board, mark, i,j-1,count)
def choose_first():
    """Randomly returns the player's mark that goes first."""
    return PLAYERS_MARKS[random.choice((0, 1))]


def space_check(board, position):
    """Returns boolean value whether the cell is free or not."""
    row,col=row_col_number(board,position)
    return board[row][col] not in PLAYERS_MARKS


def full_board_check(board):
    """Returns boolean value whether the game board is full of game marks."""
    np_array = np. unique (PLAY_BOARD)
    return len(np_array)== 2

def player_choice(board, player_mark):
    """Gets player's next position and check if it's appropriate to play."""
    position=0
    while position not in [num for num in range(1, Rows*Colls+1)]:
        try:
            if player_mark=="PC":
                while True:
                    position =random.randint(1,Rows*Colls)
                    print(position)
                    if space_check(board, position):
                        print(f'Player "{player_mark}", choose position "{position}": ')
                        break
            elif player_mark=="X":
                position = int(input(f'Player "{player_mark}", choose your next position from 1 to {Rows*Colls}: '))
                print('2X:',position)
        except ValueError as exc:
            print(f'Wrong value: {exc}. Please, try again.')
    position -= 1
    if space_check(board, position):
        return position

    return False

def replay():
    """Asks the players to play again."""
    decision = ''
    while decision not in ('y', 'n'):
        decision = input('Would you like to play again? Type "y" or "n"').lower()
    return decision == 'y'


def clear_screen():
    """Clears the game screen via adding new rows."""
    print('\n' * 100)


def switch_player(mark):
    """Switches player's marks to play next turn."""
    return 'PC' if mark == 'X' else 'X'


def check_game_finish(board, mark, position):
    """Return boolean value is the game finished or not."""
    row,col=row_col_number(board,position)
    print(row,col)
    if win_check(board, mark, row, col, count=0)==Rows:
        print(f'The player with the mark "{mark}" lost!')
        return True

    if full_board_check(PLAY_BOARD):
        print('The game ended in a draw.')
        return True

    return False
print('Welcome!')

PLAYER_MARKS = player_input()
CURRENT_PLAYER_MARK = choose_first()

print(f'Player with mark "{CURRENT_PLAYER_MARK}" goes first.')

while True:
    display_board(PLAY_BOARD)

    print(f'Turn of the player with the mark "{CURRENT_PLAYER_MARK}":')

    PLAYER_POSITION = player_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)
    place_marker(PLAY_BOARD, CURRENT_PLAYER_MARK, PLAYER_POSITION)

    if check_game_finish(PLAY_BOARD, CURRENT_PLAYER_MARK,PLAYER_POSITION ):
        display_board(PLAY_BOARD)
        if not replay():
            break
        else:
            PLAY_BOARD=[]
            for i in range(Rows):
               row = []
               for j in range(Colls):
                   row.append(i*Rows + j)
               PLAY_BOARD.append(row)
            PLAYER_MARKS = player_input()
            CURRENT_PLAYER_MARK = choose_first()
    else:
        CURRENT_PLAYER_MARK = switch_player(CURRENT_PLAYER_MARK)
    clear_screen()
