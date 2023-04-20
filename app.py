from flask import Flask, request, render_template, redirect
from game_functions import *

app = Flask(__name__)

#Setting up boards
empty_board = {
    'a1': ' - ', 'a2': ' - ', 'a3': ' - ',
    'b1': ' - ', 'b2': ' - ', 'b3': ' - ',
    'c1': ' - ', 'c2': ' - ', 'c3': ' -'
}

board = {
    'a1': ' - ', 'a2': ' - ', 'a3': ' - ',
    'b1': ' - ', 'b2': ' - ', 'b3': ' - ',
    'c1': ' - ', 'c2': ' - ', 'c3': ' - '
}

#Setting up players
player1 = 'Player 1'
player2 = 'Player 2'
player1_wins = 0
player2_wins = 0

current_player = player1

#Move lists
accepted_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
used_moves = []

#Define the home page route
@app.route('/', methods=['GET', 'POST'])
def tic_tac_toe():
    global current_player
    global player1_wins
    global player2_wins
    global board
    global used_moves

    #Check if there is a winner or a tie
    winner = check_win(player1, player2, board)

    reset_button = request.form.get('play_again')
    play_again = check_play_again(reset_button)
    if play_again:
        board = empty_board.copy()
        used_moves = []

    reset_wins = request.form.get('reset_wins')
    if reset_wins == 'True':
        player1_wins = 0
        player2_wins = 0

    #If the request method is POST, then a move has been made
    if request.method == 'POST':

        if winner != None or used_moves == 9:
            return render_template('index.html', board = board, winner = winner, tie = True, player1_wins = player1_wins, player2_wins = player2_wins, current_player = current_player, player1 = player1, player2 = player2)

        position = request.form.get('position')

        #Check if the move is valid
        if position not in accepted_moves or position in used_moves:
            return render_template('index.html', board = board, current_player = current_player, player1 = player1, player2 = player2)

        #Update the board with the move
        if current_player == player1:
            board[position] = ' X '
        else:
            board[position] = ' O '
        used_moves.append(position)

        #Check if there is a winner or a tie
        winner = check_win(player1, player2, board)
        if winner != None:
            if winner == player1:
                player1_wins += 1
            else:
                player2_wins += 1
            return render_template('index.html', board = board, winner = winner, player1_wins = player1_wins, player2_wins = player2_wins, player1 = player1, player2 = player2)
        elif len(used_moves) == 9:
            return render_template('index.html', board = board, tie = True, player1 = player1, player2 = player2)

        #Switch to the other player's turn
        current_player = current_turn(player1, player2, current_player)

    #Render the home page
    return render_template('index.html', board=board, current_player = current_player, player1 = player1, player2 = player2)

if __name__ == '__main__':
    app.run(debug=True)