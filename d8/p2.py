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

    return dp

def countVisibleTrees(grid):
    # count the perimeter
    n = len(grid)
    m = len(grid[0])

    # [left, top, right, bottom]
    dp = initialiseDp(grid, n, m)

    for i in range(n):
        # left to right
        stack = [0]
        for j in range(1, m):
            while stack and grid[i][stack[-1]] < grid[i][j]:
                stack.pop()
            
            dp[i][j][0] = j - stack[-1] if stack else j
            stack.append(j)
        
        # right to left
        stack = [m-1]
        for j in range(m - 2, -1, -1):
            while stack and grid[i][stack[-1]] < grid[i][j]:
                stack.pop()
            
            dp[i][j][2] = stack[-1] - j if stack else m - j - 1
            stack.append(j)

    # print(dp)

    for j in range(m):
        # top to bottom
        stack = [0]
        for i in range(1, n):
            while stack and grid[stack[-1]][j] < grid[i][j]:
                stack.pop()

            dp[i][j][1] = i - stack[-1] if stack else i
            stack.append(i)

        # bottom to top
        stack = [n - 1]
        for i in range(n-2, -1, -1):
            while stack and grid[stack[-1]][j] < grid[i][j]:
                stack.pop()
            
            dp[i][j][3] = stack[-1] - i if stack else n - i - 1
            stack.append(i)

    # print(dp)
    res = 0

    for i in range(1, n-1):
        for j in range(1, m-1):
            dist = 1
            for k in range(4):
                dist *= dp[i][j][k]
            
            if dist > res:
                res = dist
    
    print(res)


def run():
    grid = parseGrid()
    countVisibleTrees(grid)

if __name__ == "__main__":
    run()