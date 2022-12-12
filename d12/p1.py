from collections import deque

def getGrid():
    grid = []
    start = None
    end = None
    a_CODE = ord('a')

    with open('input.in', 'r') as reader:
        line = reader.readline()
        while line != '':
            row = []
            for char in line.strip():
                if char == 'S':
                    start = (len(grid), len(row))
                    row.append(0)
                elif char == 'E':
                    end = (len(grid), len(row))
                    row.append(25)
                else:
                    row.append(ord(char) - a_CODE)
            
            grid.append(row)
            line = reader.readline()

    return grid, start, end

def getShortestPath(grid: list[list[str]], start: tuple[int], end: tuple[int]):
    n = len(grid)
    m = len(grid[0])
    minSteps = 0

    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    visited = set()

    visited.add((0, 0))
    queue = deque([start])
    steps = 0

    while queue:
        length = len(queue)

        for _ in range(length):
            r, c = queue.popleft()

            if r == end[0] and c == end[1]:
                minSteps = steps
                break

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] - grid[r][c] < 2 and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))

        steps += 1
    
    return minSteps


def run():
    grid, start, end = getGrid()
    print(grid, start, end)
    res = getShortestPath(grid, start, end)
    print(res)

if __name__ == "__main__":
    run()