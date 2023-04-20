def current_turn(player1, player2, current_player):
    previous_player = current_player

    if previous_player == player2:
        current_player = player1
    else:
        current_player = player2

    return current_player 

def check_win(player1, player2, board):
    letters = ['a', 'b', 'c']
    winning_player = None

    for letter in letters:
        if board[f'{letter}1'] == board[f'{letter}2'] == board[f'{letter}3'] and board[f'{letter}1'] != ' - ':
            if board[f'{letter}1'] == ' X ':
                winning_player = player1
            else: 
                winning_player = player2
    
    for num in range(1, len(letters) + 1):
        if board[f'a{num}'] == board[f'b{num}'] == board[f'c{num}'] and board[f'a{num}'] != ' - ':
            if board[f'a{num}'] == ' X ':
                winning_player = player1
            else: 
                winning_player = player2

    if (board['a1'] == board['b2'] == board['c3'] or board['a3'] == board['b2'] == board['c1']) and board[f'b2'] != ' - ':
            if board[f'b2'] == ' X ':
                winning_player = player1
            else: 
                winning_player = player2

    return winning_player

def check_play_again(reset_button):
    play_again = False

    if reset_button == 'yes':
        play_again = True

    return play_again