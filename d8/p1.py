def parseGrid():
    grid = []
    with open('input.in', 'r') as reader:
        line = reader.readline().strip()
        while line != '':
            grid.append(list(map(int, list(line))))
            line = reader.readline().strip()
    return grid

def initialiseDp(grid, n, m):
    # left, top, right, bottom
    dp = [[[0] * 4 for _ in range(m)] for _ in range(n)]

    # top left
    dp[0][0][0] = grid[0][0]
    dp[0][0][1] = grid[0][0]

    # bottom left
    dp[n-1][0][0] = grid[n-1][0]
    dp[n-1][0][3] = grid[n-1][0]

    # top right
    dp[0][m-1][1] = grid[0][m-1]
    dp[0][m-1][2] = grid[0][m-1]

    # bottom right
    dp[n-1][m-1][2] = grid[n-1][m-1]
    dp[n-1][m-1][3] = grid[n-1][m-1]

    # initialise left and right column
    for i in range(n):
        dp[i][0][0] = grid[i][0]
        dp[i][m-1][2] = grid[i][m-1]
    
    # initialise top and bottom row
    for i in range(m):
        dp[0][i][1] = grid[0][i]
        dp[n-1][i][3] = grid[n-1][i]

    return dp

def countVisibleTrees(grid):
    # count the perimeter
    n = len(grid)
    m = len(grid[0])

    # [left, top, right, bottom]
    dp = initialiseDp(grid, n, m)
    
    # start from top left
    for i in range(1, n-1):
        for j in range(1, m-1):
            # left
            dp[i][j][0] = max(grid[i][j], dp[i][j-1][0])
            # top
            dp[i][j][1] = max(grid[i][j], dp[i-1][j][1])
    
    # start from bottom right
    for i in range(n-2, 0, -1):
        for j in range(m-2, 0, -1):
            # right
            dp[i][j][2] = max(grid[i][j], dp[i][j+1][2])
            # bottom
            dp[i][j][3] = max(grid[i][j], dp[i+1][j][3])

    # get the counts
    count = (n + m) * 2 - 4

    for i in range(1, n-1):
        for j in range(1, m-1):
            if grid[i][j] > dp[i][j-1][0] or grid[i][j] > dp[i-1][j][1] or grid[i][j] > dp[i][j+1][2] or grid[i][j] > dp[i+1][j][3]:
                count += 1

    print(count)

def run():
    grid = parseGrid()
    countVisibleTrees(grid)

if __name__ == "__main__":
    run()