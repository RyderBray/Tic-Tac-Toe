from game_functions import *

running = True
player1 = input('Enter player 1\'s name: ')
player2 = input('Enter player 2\'s name: ')

current_player = player2

accepted_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
used_moves = []

board = {
    'a1': ' - ', 'a2': ' - ', 'a3': ' - ',
    'b1': ' - ', 'b2': ' - ', 'b3': ' - ',
    'c1': ' - ', 'c2': ' - ', 'c3': ' -'
}

print('Play by typing a1, a2, a3, etc. Letters define which row, numbers define which spot within the row.')
while running:
    for num in range(1,10):
        game_board(board)
        current_player = current_turn(player1, player2, current_player)         #Defines current player and sets previous

        if current_player == player1:                                           #Runs function for player input based on current player
            player1_move = player_one_turn(player1, accepted_moves, used_moves, board)
        else:
            player2_move = player_two_turn(player2, accepted_moves, used_moves, board)

        winning_player = check_win(player1, player2, board)                     #Checks for winner and sets winner as winning_player if there is one

        if winning_player != None:                                              #Checks if winning_player is empty or not, if not prints winner and ends game
            print(f'{winning_player} wins!')
            running = False
            break

        if num == 9 and winning_player == None:                                 #Checks if there is no winner and board is filled, calls draw and ends game
            print('Draw!')
            running = False
            break
else:
    game_board(board)
    print('Thanks for playing!')