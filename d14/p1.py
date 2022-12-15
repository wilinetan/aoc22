def getCoord(s: str):
    return tuple(map(int, s.split(',')))

def getFormation():
    maxY = 0
    rocks = set()

    with open('input.in', 'r') as reader:
        line = reader.readline()

        while line != '':
            coords = list(map(getCoord, line.strip().split(' -> ')))

            rocks.add(coords[0])
            maxY = max(maxY, coords[0][1])

            for i in range(1, len(coords)):
                dx = coords[i][0] - coords[i-1][0]
                dy = coords[i][1] - coords[i-1][1]

                xDirection = -1 if dx < 0 else 1
                yDirection = -1 if dy < 0 else 1

                for j in range(1, abs(dx) + 1):
                    rocks.add((coords[i-1][0] + j * xDirection, coords[i-1][1]))

                for j in range(1, abs(dy) + 1):
                    y = coords[i-1][1] + j * yDirection
                    maxY = max(y, maxY)
                    rocks.add((coords[i-1][0], y))

            line = reader.readline()

    return rocks, maxY

def getSandRestPosition(rocks: set, maxY: int):
    dirs = [(0, 1), (-1, 1), (1, 1)]
    curr = [500, 0]

    while True:
        isMoved = False
        for dx, dy in dirs:
            x = curr[0] + dx
            y = curr[1] + dy

            if y > maxY:
                return [x, y]

            if (x, y) in rocks:
                continue
                
            # we move to this new position
            curr[0] = x
            curr[1] = y

            isMoved = True
            break

        if not isMoved:
            # we found the ending position
            return curr

    return curr

def getSandUnits(rocks: set, maxY: int):
    count = 0

    while True:
        # print(f'count: {count}')
        res = getSandRestPosition(rocks, maxY)
        # print(f'res: {res}')
        if res[1] > maxY:
            break
        
        count += 1
        rocks.add(tuple(res))

    print(count)

def run():
    rocks, maxY = getFormation()
    print(rocks, maxY)
    getSandUnits(rocks, maxY)

if __name__ == "__main__":
    run()