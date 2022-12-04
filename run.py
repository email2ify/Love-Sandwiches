# ------- Global Variables -------

# Our New Game Board
board = ["*", "*", "*",
         "*", "*", "*",
         "*", "*", "*"]

# Game in progress / finsihed
ongoing_game = True

# Game winner
winner = None

# Current Player (X starts first)
current_player = "X"

# ------- Classes -------


class Error(Exception):
    """Base class for other exceptions"""
    pass


class SpaceTakenError(Error):
    """Raised when the input space is already taken"""
    pass

# ------- Functions -------


def y_n_prompt():
    """ Prompts the user with a Y/N question
    to play another game
    """
    start = input("Would you like to play a game? Y/N: ").upper()
    while True:
        try:
            if start != "Y":
                if start != "N":
                    raise ValueError
        except ValueError:
            print("\n")
            print("Invalid character, Please try again")
            y_n_prompt()
        else:
            if start.upper() == "Y":
                play_game()
            elif start.upper() == "N":
                print("\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Find me on GitHub, TechCentreUK")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\n")
                exit()


def play_again():
    print("\n")
    """ Ask user for another game,
    if yes resets board
    and if no exits out
    """
    play = input("Would you like to play another game? Y/N: ").upper()
    while True:
        try:
            if play != "Y":
                if play != "N":
                    raise ValueError
        except ValueError:
            print("\n")
            print("Invalid character, Please try again")
            y_n_prompt()
        else:
            if play.upper() == "Y":
                global board
                board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
                global ongoing_game
                ongoing_game = True
                global current_player
                current_player = "X"
                global winner
                winner = None
                play_game()
            elif play.upper() == "N":
                print("\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Find me on GitHub, TechCentreUK")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\n")
                exit()


def swap_player():
    """ Swap the current player from X to O, or O to X """
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def check_for_tie():
    """
    Check for a winner and if any spaces left
    if no winner and no spaces then returns a tie
    """
    global ongoing_game
    check_for_winner()
    if "*" not in board and winner is None:
        ongoing_game = False
        print("Game is a Tie! \n")
        play_again()
        return True
    else:
        return False


def check_diagonals():
    """
    Check all diagonal rows for a winner
    if no winner then returns None
    """
    global ongoing_game
    diagonal_1 = board[0] == board[4] == board[8] != "*"
    diagonal_2 = board[2] == board[4] == board[6] != "*"
    if diagonal_1 or diagonal_2:
        ongoing_game = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


def check_columns():
    """
    Check all columns for a winner
    if no winner then returns None
    """
    global ongoing_game
    column_1 = board[0] == board[3] == board[6] != "*"
    column_2 = board[1] == board[4] == board[7] != "*"
    column_3 = board[2] == board[5] == board[8] != "*"
    if column_1 or column_2 or column_3:
        ongoing_game = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None


def check_rows():
    """
    Check all rows for a winner
    if no winner then returns None
    """
    global ongoing_game
    row_1 = board[0] == board[1] == board[2] != "*"
    row_2 = board[3] == board[4] == board[5] != "*"
    row_3 = board[6] == board[7] == board[8] != "*"
    if row_1 or row_2 or row_3:
        ongoing_game = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_for_winner():
    """ Check all possible outcomes for a winner """
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_if_game_over():
    """ Check the game for a winner or tie """
    check_for_winner()
    check_for_tie()


def handle_turn(player):
    """
    Loops through players turns and
    handles exception errors appropriately
    """
    print(player + "'s turn.")
    valid = False
    position = input("\nChoose a position from 1-9: ")
    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while not valid:
        try:
            if position not in x:
                raise ValueError
            else:
                position = int(position) - 1
                if board[position] == "*":
                    valid = True
                    board[position] = player
                    display_board()
                    return
                else:
                    raise SpaceTakenError
        except ValueError:
            print("\nError: Incorrect Value Please Try Again\n")
            position = input("\nChoose a position from 1-9: ")
        except SpaceTakenError:
            print("\nError: Space Taken, Try Again\n")
            position = input("\nChoose a position from 1-9: ")


def display_board():
    """ Displays the game board """
    print("\n")
    print("-------------------------------------")
    print("|  " + board[0] + " | " + board[1] +
          " | " + board[2] + "             1 | 2 | 3  |")
    print("|  " + board[3] + " | " + board[4] +
          " | " + board[5] + "  TicTacToe  4 | 5 | 6  |")
    print("|  " + board[6] + " | " + board[7] +
          " | " + board[8] + "             7 | 8 | 9  |")
    print("-------------------------------------")
    print("\n")


def play_game():
    """Play a game of tic tac toe, game displays the board,
    loops the turns whilst game is in session then checks the
    game is over. If game is ongoing then swaps player until a winner.
    """
    display_board()
    while ongoing_game:
        handle_turn(current_player)
        check_if_game_over()
        swap_player()
        global board
        if winner == "X" or winner == "O":
            print("<-------- Congratulations " +
                  winner + ", you win. -------->")
            play_again()


def start():
    """ Prompt user for a game of tic tac toe """
    display_board()
    print("\n")
    y_n_prompt()


# ------- Execute -------

# Start a game of tic tac toe
print("\nWelcome to Clayton's TicTacToe Multiplayer Game")
start()
