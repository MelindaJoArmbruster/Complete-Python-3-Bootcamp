import os
import random


def display_board(board):
    os.system('clear')

    print('\n')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').capitalize()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def place_marker(board, marker, position):
    board[position] = marker


def space_check(board, position):
    return board[position] != 'X' and board[position] != 'O'


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    return position


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def replay():
    play_again = input('Do you want to play again? Enter y or n: ')
    if play_again == 'y':
        return True
    else:
        return False


def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(board)
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        # Player 1 Turn
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            # Player 2 Turn
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 1'

            # pass

    if not replay():
        break
