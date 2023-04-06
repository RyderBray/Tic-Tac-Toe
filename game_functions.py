def current_turn(player1, player2, current_player):
    previous_player = current_player

    if previous_player == player2:
        current_player = player1
    else:
        current_player = player2

    return current_player

def player_one_turn(player1, accepted_moves, used_moves, board):
    player1_str = input(f'{player1}\'s turn: ')
    valid_move = False

    while valid_move == False:
        if player1_str in accepted_moves and not player1_str in used_moves:
            valid_move = True
            used_moves.append(player1_str)
        else:
            player1_str = input(f'Please re-enter a valid move: ')

    player1_move = board.update({f'{player1_str}' : ' X '})

    return player1_move

def player_two_turn(player2, accepted_moves, used_moves, board):
    player2_str = input(f'{player2}\'s turn: ')
    valid_move = False

    while valid_move == False:
        if player2_str in accepted_moves and not player2_str in used_moves:
            valid_move = True
            used_moves.append(player2_str)
        else:
            player2_str = input(f'Please re-enter a valid move: ')

    player2_move = board.update({f'{player2_str}' : ' O ' })

    return player2_move     

def game_board(board):
    print(f"{board['a1']}|{board['a2']}|{board['a3']}")
    print(f"{board['b1']}|{board['b2']}|{board['b3']}")
    print(f"{board['c1']}|{board['c2']}|{board['c3']}")

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

    if board['a1'] == board['b2'] == board['c3'] or board['a3'] == board['b2'] == board['c1'] and board[f'b2'] != ' - ':
            if board[f'b2'] == ' X ':
                winning_player = player1
            else: 
                winning_player = player2

    return winning_player