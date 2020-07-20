# ------Global Variable--------------
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]
# If game is still going
game_is_running = True

# Who won? or tie?
winner = None

# Whose turn is it?
current_player = "X"


def disp_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():
    # display initial board
    disp_board()

    while game_is_running:
        handle_turn(current_player)

        check_game_is_over()

        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")


def handle_turn(player):
    print(player + " 's turn.")
    position = input("choose a position from 1-9:")

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid input. Choose a position from 1-9:")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
           print("try another postion.")

    board[position] = player

    disp_board()


def check_game_is_over():
    check_win()
    check_tie()


def check_win():
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return


def check_rows():
    global game_is_running

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_is_running = False
    # Return the winner
    if row_1:
      return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_is_running

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_is_running = False
    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    global game_is_running

    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[6] == board[4] == board[2] != "-"


    # If any row does have a match, flag that there is a win
    if diag_1  or diag_2:
        game_is_running = False
    # Return the winner
    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]
    return


def check_tie():
    global game_is_running
    if "-" not in board:
        game_is_running = False
        return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return


play_game()

# create a board
# display board
# play game
# check win
# check rows
# check columns
# check diagonals
# check tie
# flip player
