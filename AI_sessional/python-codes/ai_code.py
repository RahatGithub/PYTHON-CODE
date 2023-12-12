grid = [[[[0 for _ in range(3)] for _ in range(3)] for _ in range(10)] for _ in range(10)]
sub_grid = [[False for _ in range(3)] for _ in range(10)]
# one, two = 0, 0
pr_bot = [(1, 1), (0, 0), (0, 2), (2, 2), (2, 0), (1, 0), (0, 1), (1, 2),
          (2, 1)]  # higher priority first for bot player
pr_input = [(1, 0), (0, 1), (1, 2), (2, 1), (0, 0), (0, 2), (2, 2), (2, 0),
            (1, 1)]  # lower priority first for user input


def print_sub_grid(x, y, z):
    print(" ".join(map(str, grid[x][y][z])), end="   ")


def print_grid():
    for i in range(3):
        # first row main grid
        print_sub_grid(0, 0, i)
        print_sub_grid(0, 1, i)
        print_sub_grid(0, 2, i)
        print()

    print()
    for i in range(3):
        # second row main grid
        print_sub_grid(1, 0, i)
        print_sub_grid(1, 1, i)
        print_sub_grid(1, 2, i)
        print()

    print()
    for i in range(3):
        # third row main grid
        print_sub_grid(2, 0, i)
        print_sub_grid(2, 1, i)
        print_sub_grid(2, 2, i)
        print()
    print()


def principle_diagonally_game_possible(x, y, val):
    if sub_grid[x][y]:
        return -1
    if grid[x][y][0][0] == grid[x][y][1][1] == val and grid[x][y][2][2] == 0:
        return 2
    if grid[x][y][0][0] == grid[x][y][2][2] == val and grid[x][y][1][1] == 0:
        return 1
    if grid[x][y][1][1] == grid[x][y][2][2] == val and grid[x][y][0][0] == 0:
        return 0
    return -1


def secondary_diagonally_game_possible(x, y, val):
    if sub_grid[x][y]:
        return -1
    if grid[x][y][0][2] == grid[x][y][1][1] == val and grid[x][y][2][0] == 0:
        return 2
    if grid[x][y][0][2] == grid[x][y][2][0] == val and grid[x][y][1][1] == 0:
        return 1
    if grid[x][y][1][1] == grid[x][y][2][0] == val and grid[x][y][0][2] == 0:
        return 0
    return -1


def first_column_game_possible(x, y, val):
    if sub_grid[x][y]:
        return -1
    if grid[x][y][0][0] == grid[x][y][1][0] == val and grid[x][y][2][0] == 0:
        return 2
    if grid[x][y][0][0] == grid[x][y][2][0] == val and grid[x][y][1][0] == 0:
        return 1
    if grid[x][y][1][0] == grid[x][y][2][0] == val and grid[x][y][0][0] == 0:
        return 0
    return -1


def second_column_game_possible(x, y, val):
    if sub_grid[x][y]:
        return -1
    if grid[x][y][0][1] == grid[x][y][1][1] == val and grid[x][y][2][1] == 0:
        return 2
    if grid[x][y][0][1] == grid[x][y][2][1] == val and grid[x][y][1][1] == 0:
        return 1
    if grid[x][y][1][1] == grid[x][y][2][1] == val and grid[x][y][0][1] == 0:
        return 0
    return -1


def third_column_game_possible(x, y, val):
    if sub_grid[x][y]:
        return -1
    if grid[x][y][0][2] == grid[x][y][1][2] == val and grid[x][y][2][2] == 0:
        return 2
    if grid[x][y][0][2] == grid[x][y][2][2] == val and grid[x][y][1][2] == 0:
        return 1
    if grid[x][y][1][2] == grid[x][y][2][2] == val and grid[x][y][0][2] == 0:
        return 0
    return -1


def first_row_game_possible(x, y, val):
    if sub_grid[x][y]:
        return -1
    if grid[x][y][0][0] == grid[x][y][0][1] == val and grid[x][y][0][2] == 0:
        return 2
    if grid[x][y][0][0] == grid[x][y][0][2] == val and grid[x][y][0][1] == 0:
        return 1
    if grid[x][y][0][1] == grid[x][y][0][2] == val and grid[x][y][0][0] == 0:
        return 0
    return -1


def second_row_game_possible(x, y, val):
    if sub_grid[x][y]:
        return -1
    if grid[x][y][1][0] == grid[x][y][1][1] == val and grid[x][y][1][2] == 0:
        return 2
    if grid[x][y][1][0] == grid[x][y][1][2] == val and grid[x][y][1][1] == 0:
        return 1
    if grid[x][y][1][1] == grid[x][y][1][2] == val and grid[x][y][1][0] == 0:
        return 0
    return -1


def third_row_game_possible(x, y, val):
    if sub_grid[x][y]:
        return -1
    if grid[x][y][2][0] == grid[x][y][2][1] == val and grid[x][y][2][2] == 0:
        return 2
    if grid[x][y][2][0] == grid[x][y][2][2] == val and grid[x][y][2][1] == 0:
        return 1
    if grid[x][y][2][1] == grid[x][y][2][2] == val and grid[x][y][2][0] == 0:
        return 0
    return -1


# def grid_center_check(x, y):
#     return grid[x][y][1][1] != 0


def sub_grid_move_possible(x, y):
    return sub_grid[x][y]


def next_game_possible(x, y, val):
    if sub_grid[x][y]:
        return True
    if principle_diagonally_game_possible(x, y, val) != -1:
        return True
    if secondary_diagonally_game_possible(x, y, val) != -1:
        return True
    if first_row_game_possible(x, y, val) != -1:
        return True
    if second_row_game_possible(x, y, val) != -1:
        return True
    if third_row_game_possible(x, y, val) != -1:
        return True
    if first_column_game_possible(x, y, val) != -1:
        return True
    if second_column_game_possible(x, y, val) != -1:
        return True
    if third_column_game_possible(x, y, val) != -1:
        return True
    return False


def sub_grid_game_possible(x, y, val):
    if sub_grid[x][y]:
        return False

    if grid[x][y][0][0] == grid[x][y][1][1] == grid[x][y][2][2] == val:
        return True

    if grid[x][y][0][2] == grid[x][y][1][1] == grid[x][y][2][0] == val:
        return True

    if grid[x][y][0][0] == grid[x][y][0][1] == grid[x][y][0][2] == val:
        return True

    if grid[x][y][1][0] == grid[x][y][1][1] == grid[x][y][1][2] == val:
        return True

    if grid[x][y][2][0] == grid[x][y][2][1] == grid[x][y][2][2] == val:
        return True

    if grid[x][y][0][0] == grid[x][y][1][0] == grid[x][y][2][0] == val:
        return True

    if grid[x][y][0][1] == grid[x][y][1][1] == grid[x][y][2][1] == val:
        return True

    if grid[x][y][0][2] == grid[x][y][1][2] == grid[x][y][2][2] == val:
        return True

    return False


def winner(value):
    if sub_grid[0][0] == sub_grid[0][1] == sub_grid[0][2] == value:
        return True
    if sub_grid[1][0] == sub_grid[1][1] == sub_grid[1][2] == value:
        return True
    if sub_grid[2][0] == sub_grid[2][1] == sub_grid[2][2] == value:
        return True

    if sub_grid[0][0] == sub_grid[1][0] == sub_grid[2][0] == value:
        return True
    if sub_grid[0][1] == sub_grid[1][1] == sub_grid[2][1] == value:
        return True
    if sub_grid[0][2] == sub_grid[1][2] == sub_grid[2][2] == value:
        return True

    if sub_grid[0][0] == sub_grid[1][1] == sub_grid[2][2] == value:
        return True
    if sub_grid[0][2] == sub_grid[1][1] == sub_grid[2][0] == value:
        return True

    return False


# ***********USER MOVE************
def user_move():
    if winner(1):
        print("Winner is Bot Player")
        return
    if winner(2):
        print("Winner is input Player")
        return

    while True:
        x, y, a, b = map(int, input("Take input for User (x y a b): ").split())
        if sub_grid[x][y]:
            print("Invalid Move: Take input again")
        elif grid[x][y][a][b] != 0:
            print("Invalid Move: Take input again")
        else:
            break

    grid[x][y][a][b] = 2
    if sub_grid_game_possible(x, y, 2):
        sub_grid[x][y] = 2

    print_grid()

    if winner(1):
        print("Winner is Bot Player")
        return
    if winner(2):
        print("Winner is input Player")
        return
    
    bot_thinking(a, b)
# ***********USER MOVE ENDS****************

# **************NEXT MOVE STARTS*************************
def next_move(pos1, pos2):
    if winner(1):
        print("Winner is Bot Player")
        return
    if winner(2):
        print("Winner is input Player")
        return

    if sub_grid[pos1][pos2]:
        return user_move()

    while True:
        print(f"User Player Move: Default Main Grid: {pos1} {pos2}")
        x, y = map(int, input("Take input for sub grid (x y): ").split())
        if grid[pos1][pos2][x][y] != 0:
            print("Invalid Move: Take input again")
        else:
            break

    grid[pos1][pos2][x][y] = 2
    if sub_grid_game_possible(pos1, pos2, 2):
        sub_grid[pos1][pos2] = 2
    a, b = x, y
    print_grid()
    bot_thinking(a, b)
# **************NEXT MOVE ENDS*************************


def check_8_steps(a, b, player):
    # Principle Diagonal
    pos = principle_diagonally_game_possible(a, b, player)
    if pos != -1:
        pos1 = pos
        pos2 = pos
        grid[a][b][pos1][pos2] = 1
        sub_grid[a][b] = 1
        print(f"Bot Player Move: Main Grid: {a} {b} Sub_Grid: {pos1} {pos2}")
        print_grid()
        if sub_grid[pos1][pos2]:
            return user_move()
        return next_move(pos1, pos2)

    # Secondary Diagonal
    pos = secondary_diagonally_game_possible(a, b, player)
    if pos != -1:
        pos1 = pos
        pos2 = 2 - pos
        grid[a][b][pos1][pos2] = 1
        sub_grid[a][b] = 1
        print(f"Bot Player Move: Main Grid: {a} {b} Sub_Grid: {pos1} {pos2}")
        print_grid()
        if sub_grid[pos1][pos2]:
            return user_move()
        return next_move(pos1, pos2)

    # Rows
    pos = first_row_game_possible(a, b, player)
    if pos != -1:
        pos1 = 0
        pos2 = pos
        grid[a][b][pos1][pos2] = 1
        sub_grid[a][b] = 1
        print(f"Bot Player Move: Main Grid: {a} {b} Sub_Grid: {pos1} {pos2}")
        print_grid()
        if sub_grid[pos1][pos2]:
            return user_move()
        return next_move(pos1, pos2)

    pos = second_row_game_possible(a, b, player)
    if pos != -1:
        pos1 = 1
        pos2 = pos
        grid[a][b][pos1][pos2] = 1
        sub_grid[a][b] = 1
        print(f"Bot Player Move: Main Grid: {a} {b} Sub_Grid: {pos1} {pos2}")
        print_grid()
        if sub_grid[pos1][pos2]:
            return user_move()
        return next_move(pos1, pos2)

    pos = third_row_game_possible(a, b, player)
    if pos != -1:
        pos1 = 2
        pos2 = pos
        grid[a][b][pos1][pos2] = 1
        sub_grid[a][b] = 1
        print(f"Bot Player Move: Main Grid: {a} {b} Sub_Grid: {pos1} {pos2}")
        print_grid()
        if sub_grid[pos1][pos2]:
            return user_move()
        return next_move(pos1, pos2)

    # Columns
    pos = first_column_game_possible(a, b, player)
    if pos != -1:
        pos1 = pos
        pos2 = 0
        grid[a][b][pos1][pos2] = 1
        sub_grid[a][b] = 1
        print(f"Bot Player Move: Main Grid: {a} {b} Sub_Grid: {pos1} {pos2}")
        print_grid()
        if sub_grid[pos1][pos2]:
            return user_move()
        return next_move(pos1, pos2)

    pos = second_column_game_possible(a, b, player)
    if pos != -1:
        pos1 = pos
        pos2 = 1
        grid[a][b][pos1][pos2] = 1
        sub_grid[a][b] = 1
        print(f"Bot Player Move: Main Grid: {a} {b} Sub_Grid: {pos1} {pos2}")
        print_grid()
        if sub_grid[pos1][pos2]:
            return user_move()
        return next_move(pos1, pos2)

    pos = third_column_game_possible(a, b, player)
    if pos != -1:
        pos1 = pos
        pos2 = 2
        grid[a][b][pos1][pos2] = 1
        sub_grid[a][b] = 1
        print(f"Bot Player Move: Main Grid: {a} {b} Sub_Grid: {pos1} {pos2}")
        print_grid()
        if sub_grid[pos1][pos2]:
            return user_move()
        return next_move(pos1, pos2)


# *******************BOT THINKING************************
def bot_thinking(a, b):

    while True:
        
        # checking if bot is winning
        check_8_steps(a, b, 1)

        # checking if user is winning
        check_8_steps(a, b, 2)

        # Check if the opponent can win in the next move and block it
        for p, q in pr_input:
            if not sub_grid[a][b] and grid[a][b][p][q] == 0 and not next_game_possible(p, q, 2):
                pos1 = p
                pos2 = q
                grid[a][b][pos1][pos2] = 1
                print(f"Bot Player Move: Main Grid: {a} {b} Sub_Grid: {pos1} {pos2}")
                print_grid()
                return next_move(pos1, pos2)

        # If no winning or blocking moves are available, make any valid move
        for p, q in pr_input:
            if not sub_grid[a][b] and grid[a][b][p][q] == 0:
                pos1 = p
                pos2 = q
                grid[a][b][pos1][pos2] = 1
                print(f"Bot Player Move: Main Grid: {a} {b} Sub_Grid: {pos1} {pos2}")
                print_grid()
                return next_move(pos1, pos2)

        # If all else fails, select a random move
        x = a
        y = b
        return wish(x, y)
#*******************BOT THINKING ENDS****************

#*******************WISH STARTS**********************
def wish(x, y):
    if winner(1):
        print("Winner is Bot Player")
        return
    if winner(2):
        print("Winner is input Player")
        return

    if sub_grid[x][y]:
        print("Bot player should choose subgrid")
        for p, q in pr_bot:
            if next_game_possible(p, q, 1) and sub_grid[p][q]:
                a, b = p, q

                #check if bot is winning
                check_8_steps(a, b, 1)

                # #check if user is winning
                # check_8_steps(a, b, 2)


        # ------------------------------------------
        # Check if the user can give a game in any main grid
        for p, q in pr_input:
            if sub_grid[p][q] and next_game_possible(p, q, 2):
                a, b = p, q

                pos = principle_diagonally_game_possible(a, b, 2)
                if pos != -1:
                    pos1 = pos
                    pos2 = pos
                    grid[a][b][pos1][pos2] = 1
                    print(f"Bot Player Move: Main Grid: {a} {b}     Sub_Grid: {pos1} {pos2}")
                    print_grid()
                    return next_move(pos1, pos2)

                pos = secondary_diagonally_game_possible(a, b, 2)
                if pos != -1:
                    pos1 = pos
                    pos2 = 2 - pos
                    grid[a][b][pos1][pos2] = 1
                    print(f"Bot Player Move: Main Grid: {a} {b}     Sub_Grid: {pos1} {pos2}")
                    print_grid()
                    return next_move(pos1, pos2)

                pos = first_row_game_possible(a, b, 2)
                if pos != -1:
                    pos1 = 0
                    pos2 = pos
                    grid[a][b][pos1][pos2] = 1
                    print(f"Bot Player Move: Main Grid: {a} {b}     Sub_Grid: {pos1} {pos2}")
                    print_grid()
                    return next_move(pos1, pos2)

                pos = second_row_game_possible(a, b, 2)
                if pos != -1:
                    pos1 = 1
                    pos2 = pos
                    grid[a][b][pos1][pos2] = 1
                    print(f"Bot Player Move: Main Grid: {a} {b}     Sub_Grid: {pos1} {pos2}")
                    print_grid(pos1, pos2)
                    return
#*******************WISH ENDS**********************


print_grid()
user_move()
