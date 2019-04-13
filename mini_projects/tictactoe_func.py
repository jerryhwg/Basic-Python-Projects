# Python 3.7.2
# Layout
# module import
# functions
# main() to call functions and control flow

from IPython.display import clear_output
import random

def display_board(board):
    clear_output() # only work in jupyter, it helps display the board only one time
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# test_board = [' ']*10
# print(test_board)
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# use ' ' to fill in board[i]
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = '' # declare an empty var

    # keep asking until player 1 chooses X or O using while loop
    while marker != 'X' and marker != 'O':
    # while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O') # tuple
    else:
        return ('O', 'X')

# player1_input, player2_input = player_input()

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):

    # ALL ROWS have the same mark
    return ((board[1] == board[2] == board[3] == mark) or # without mark, all 3 blank case even be the WIN case
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    # ALL COLUMNS have the same mark
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    # Diagnoal
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))

def choose_first():
    flip = random.randint(0,1) # tail or head
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' ' # check if the position is empty then return True

def full_board_check(board):

    for i in range(1,10): # 1 ~ 9
        if space_check(board,i): # if True, then board is not full
            return False
    return True # otherwise the board is full

def player_choice(board):

    position = 0
    # keep asking until true
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position): # continue to run 'position' if the choice is not in 1~9 or no empty position
        position = int(input('Choose a position: (1-9) '))
    return position

def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y') # if yes, True = replay
    # choice = input("Play again? Enter Yes or No")
    # return choice == 'Yes'

# Main game

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input() # (X, O) or (O, Y)
    turn = choose_first() # Player 1 or Player 2
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker): # if win_check = True, game ends
                display_board(theBoard)
                print('You won the game')
                game_on = False # exit while loop
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                    break # exit the top loop (while loop)
                else:
                    turn = 'Player 2'

        else: # same logics but for the player 2
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 1'

    if not replay(): # if return of replay() is False
        break # exit the main while loop (exit game)