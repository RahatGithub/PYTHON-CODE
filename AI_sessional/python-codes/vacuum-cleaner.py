# ***Vacuum Cleaner by BFS and DFS***

from collections import deque

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]
grid = [[0] * 10 for _ in range(10)]
vis = [[0] * 10 for _ in range(10)]
bfsC = 0
dfsC = 0
tot = 11
totC = 0

def bfs():
    global bfsC, totC
    q = deque([(9, 0)])
    vis[9][0] = 1

    while q:
        bfsC += 1
        x, y = q.popleft()

        if grid[x][y] == 1:
            grid[x][y] = 0
            totC += 1
            if totC == tot:
                return
        
        for d in range(4):
            curx, cury = x + dx[d], y + dy[d]
            if 0 <= curx < 10 and 0 <= cury < 10 and vis[curx][cury] == 0:
                q.append((curx, cury))
                vis[curx][cury] = 1

def dfs(x, y):
    global dfsC, totC
    dfsC += 1

    if grid[x][y] == 1:
        grid[x][y] = 0
        totC += 1
        if totC == tot:
            return

    if vis[x][y] == 1:
        return
    else:
        vis[x][y] = 1

    for d in range(4):
        curx, cury = x + dx[d], y + dy[d]
        if 0 <= curx < 10 and 0 <= cury < 10 and vis[curx][cury] == 0 and tot != totC:
            dfs(curx, cury)

def main():
    global totC, bfsC, dfsC, grid, vis
    # marking the cells that have dirt by setting the value 1
    grid[0][3] = grid[0][9] = grid[1][1] = grid[1][5] = grid[3][4] = grid[3][8] = grid[5][1] = grid[6][7] = grid[8][6] = grid[9][2] = grid[9][8] = 1

    bfs()
    print("BFS Cost:", bfsC, "\n")

    # reinitializing the value of visited cells to 0
    vis = [[0] * 10 for _ in range(10)]

    totC = 0

    grid = [[0] * 10 for _ in range(10)]
    grid[0][3] = grid[0][9] = grid[1][1] = grid[1][5] = grid[3][4] = grid[3][8] = grid[5][1] = grid[6][7] = grid[8][6] = grid[9][2] = grid[9][8] = 1

    dfs(9, 0)
    print("DFS Cost:", dfsC, "\n")

if __name__ == "__main__":
    main()