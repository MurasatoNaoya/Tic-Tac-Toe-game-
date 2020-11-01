import random

def display_board(board):

    print('|' + board[0] + '|' + board[1] +'|'+ board[2] +'|')
    print('|' + board[3] + '|' + board[4] +'|' + board[5] +'|')
    print('|' + board[6] + '|' + board[7] +'|' + board[8] +'|')


def player_input():
    
    marker = ''
    while not (marker == 'X' or marker == 'O'): # Instead of this, you could use 'while not' with both conditions being ==X and ==O instead of using the != operator. 
        marker = input('Player 1, please choose X or O: ').upper()
    
        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker # This function simply assigns the cross or circle to the desired place.


def win_check(board,mark):
   return ((board[0] == mark and board[1] == mark and board[2] == mark) or # across the top
    (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
    (board[6] == mark and board[7] == mark and board[8] == mark) or # across the bottom
    (board[1] == mark and board[4] == mark and board[7] == mark) or # down the middle
    (board[0] == mark and board[3] == mark and board[6] == mark) or # down the left side
    (board[2] == mark and board[5] == mark and board[8] == mark) or # down the right side
    (board[0] == mark and board[4] == mark and board[8] == mark) or # diagonal
    (board[6] == mark and board[4] == mark and board[2] == mark)) # diagonal




def choose_first():
    flip = random.randint(0,1)
    if flip == 1:                           
        return 'Player 1'
    else:
        return 'Player 2'

def space_check (board, position):
    return board[position] == ' '

def full_board_check(board):
    for index in range(1,9):
        if space_check(board,index):
            return False
        
    return True

def player_choice(board):
    position = None
    acceptable_range = [0,1,2,3,4,5,6,7,8]
    while not (position in acceptable_range) or not (space_check(board, position)): # Uniary operator. 
        position = int(input('Choose a position: 0-8: '))
    
    print('Loop complete')
    return position

def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y') # This will returna boolean if the lowercase inputted value, starts with a 'y'.



# Now that we have the puzzle pieces of functions that will make up our game, now we have to put the game together. 

print('Welcome to Tic-Tac-Toe')

# Initiate the game. 

# Play the game
# 
# Set the conditions, i.e  - Who goes first, which player has which symbol etc.. 



while True:

    empty_board = [' ']*9
    player_1_input, player_2_input = player_input()
    turn = choose_first()
    print(turn + ' will be going first.')

    play_game = input('Ready to play? Yes or No: ')

    if play_game[0].lower() == 'y':
        game_on = True
    else: 
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
    
            display_board(empty_board)
            position = player_choice(empty_board)
            place_marker(empty_board, player_1_input, position)
        
            if win_check(empty_board, player_1_input):
                display_board(empty_board)
                print('Well done Player 1! You have won.')
                game_on = False
            else:
                if full_board_check(empty_board):
                    display_board(empty_board)  
                    print('HIKIWAKE!')
                    break
                else: turn = 'Player 2'

        else:
            display_board(empty_board)
            position = player_choice(empty_board)
            place_marker(empty_board, player_2_input, position)
        
            if win_check(empty_board, player_2_input):
                display_board(empty_board)
                print('Well done Player 2! You have won.')
                game_on = False
            else:
                if full_board_check(empty_board):
                    display_board(empty_board)
                    print('HIKIWAKE!')
                    break
                else: 
                    turn = 'Player 1'



    if not replay():
        break