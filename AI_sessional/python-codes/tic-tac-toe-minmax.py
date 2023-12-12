# Tic-Tac-Toe with Minmax

grid = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]
player = 'x'
opponent = 'y'
best_val = -100


def print_grid():
    for row in grid:
        for cell in row:
            if cell == 'x':
                print("X ", end="")
            elif cell == 'y':
                print("O ", end="")
            else:
                print("_ ", end="")
        print()
    print()


def utility(ch):
    mx = -100
    # 3 rows
    if grid[0][0] == ch and grid[0][1] == ch and grid[0][2] == ch:
        mx = max(mx, 24)
    if grid[1][0] == ch and grid[1][1] == ch and grid[1][2] == ch:
        mx = max(mx, 26)
    if grid[2][0] == ch and grid[2][1] == ch and grid[2][2] == ch:
        mx = max(mx, 24)

    # 3 columns
    if grid[0][0] == ch and grid[1][0] == ch and grid[2][0] == ch:
        mx = max(mx, 24)
    if grid[0][1] == ch and grid[1][1] == ch and grid[2][1] == ch:
        mx = max(mx, 26)
    if grid[0][2] == ch and grid[1][2] == ch and grid[2][2] == ch:
        mx = max(mx, 24)

    # diagonals
    if grid[0][0] == ch and grid[1][1] == ch and grid[2][2] == ch:
        mx = max(mx, 36)
    if grid[2][0] == ch and grid[1][1] == ch and grid[0][2] == ch:
        mx = max(mx, 36)

    # all possible moves for row 1 where 2 indices are equal
    if grid[0][0] == ch and grid[0][1] == ch:
        mx = max(mx, 10)
    if grid[0][0] == ch and grid[1][0] == ch:
        mx = max(mx, 10)
    if grid[0][0] == ch and grid[1][1] == ch:
        mx = max(mx, 20)

    if grid[0][1] == ch and grid[0][2] == ch:
        mx = max(mx, 10)
    if grid[0][1] == ch and grid[1][1] == ch:
        mx = max(mx, 18)
    if grid[0][1] == ch and grid[1][2] == ch:
        mx = max(mx, 6)
    if grid[0][1] == ch and grid[1][0] == ch:
        mx = max(mx, 6)

    if grid[0][2] == ch and grid[1][2] == ch:
        mx = max(mx, 10)
    if grid[0][2] == ch and grid[1][1] == ch:
        mx = max(mx, 20)

    # all possible moves for row 2 where 2 indices are equal
    if grid[1][0] == ch and grid[1][1] == ch:
        mx = max(mx, 18)
    if grid[1][0] == ch and grid[2][0] == ch:
        mx = max(mx, 10)
    if grid[1][0] == ch and grid[2][1] == ch:
        mx = max(mx, 6)

    if grid[1][1] == ch and grid[1][2] == ch:
        mx = max(mx, 18)
    if grid[1][1] == ch and grid[2][1] == ch:
        mx = max(mx, 18)
    if grid[1][1] == ch and grid[2][2] == ch:
        mx = max(mx, 20)
    if grid[1][1] == ch and grid[2][0] == ch:
        mx = max(mx, 20)

    if grid[1][2] == ch and grid[2][2] == ch:
        mx = max(mx, 10)
    if grid[1][2] == ch and grid[2][1] == ch:
        mx = max(mx, 6)

    # all possible moves for row 3 where 2 indices are equal
    if grid[2][0] == ch and grid[2][1] == ch:
        mx = max(mx, 10)
    if grid[2][2] == ch and grid[2][1] == ch:
        mx = max(mx, 10)

    # all possible moves for index 1
    if grid[0][1] == ch or grid[1][0] == ch or grid[1][2] == ch or grid[2][1] == ch:
        mx = max(mx, 2)
    if grid[0][0] == ch or grid[0][2] == ch or grid[2][0] == ch or grid[2][2] == ch:
        mx = max(mx, 4)

    if grid[1][1] == ch:
        mx = max(mx, 8)

    return mx


def calc():
    mx_x = utility(player)
    mx_y = utility(opponent)
    return mx_x - mx_y


def is_moves_left():
    for row in grid:
        if '_' in row:
            return True
    return False


def minimax(is_max):
    if not is_moves_left():
        res = calc()
        return res

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if grid[i][j] == '_':
                    grid[i][j] = player
                    best = max(best, minimax(not is_max))
                    grid[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if grid[i][j] == '_':
                    grid[i][j] = opponent
                    best = min(best, minimax(not is_max))
                    grid[i][j] = '_'
        return best


if __name__ == '__main__':
    for i in range(3):
        for j in range(3):
            if grid[i][j] == '_':
                grid[i][j] = player
                move_val = minimax(False)
                grid[i][j] = '_'
                best_val = max(best_val, move_val)

    print(best_val)