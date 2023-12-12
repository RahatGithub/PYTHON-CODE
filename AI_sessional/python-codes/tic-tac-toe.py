# ***Tic-Tac-Toe***

import random

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Function to check if the board is full
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


# Function to check if the move can lead to a winning step
def check_winning_move(board, row, col, player):
    # Check for horizontal match
    if board[row][(col + 1) % 3] == board[row][(col + 2) % 3] == player:
        return True
    # Check for vertical match
    if board[(row + 1) % 3][col] == board[(row + 2) % 3][col] == player:
        return True
    # Check for diagonal match 
    if row == col or row + col == 2:
        if board[(row + 1) % 3][(col + 1) % 3] == board[(row + 2) % 3][(col + 2) % 3] == player:
            return True
        if board[(row + 1) % 3][(col + 2) % 3] == board[(row + 2) % 3][(col + 1) % 3] == player:
            return True
    return False


# Function to get the optimal move for the agent
def get_optimal_move(board):
    # Check if the middle position is empty
    if board[1][1] == ' ':
        return 1, 1

    # Check if any corner position is empty 
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
#     random.shuffle(corners)
    for corner in corners:
        if board[corner[0]][corner[1]] == ' ':
            return corner[0], corner[1]

    # If no corner moves possible then return the first empty cell found
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return row, col


# Function to get the defensive move
def get_defensive_move(board, opponent):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ' and check_winning_move(board, row, col, opponent):
                return row, col


# Function to check if there's a winning move for the player
def get_winning_move(board, player):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ' and check_winning_move(board, row, col, player):
                return row, col
    return None  # Return None if there's no winning move


# Function to get the user's move
def get_user_move(board):
    while True:
#         row = int(input("Enter row (0-2): "))
#         col = int(input("Enter column (0-2): "))
        row, col = map(int, input("Your move(row[SPACE]col): ").split(" "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            return row, col
        else:
            print("INVALID MOVE!")


# Function to play Tic-Tac-Toe with the agent
def play():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    # Agent's first move
    row, col = get_optimal_move(board)
    board[row][col] = players[current_player]

    while not is_board_full(board):
        current_player = 1 - current_player
        print_board(board)

        # User's move
        if current_player == 1:
            print(f"User's({players[current_player]}) turn:")
            row, col = get_user_move(board) # taking input from the user
            board[row][col] = players[current_player]

            # Check if user wins
            if check_winning_move(board, row, col, players[current_player]):
                print_board(board)
                print(f"User({players[current_player]}) wins!")
                return

        # Agent's move
        if current_player == 0:
            print("Agent's turn: ")
            winning_move = get_winning_move(board, players[current_player])
            if winning_move is not None:
                row, col = winning_move
            else:
                defensive_move = get_defensive_move(board, players[1 - current_player])
                if defensive_move is not None:
                    row, col = defensive_move
                else:
                    row, col = get_optimal_move(board)

            board[row][col] = players[current_player]

            # Check if agent wins
            if check_winning_move(board, row, col, players[current_player]):
                print_board(board)
                print(f"The agent({players[current_player]}) wins!")
                return

        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            return


# Play the game
play()