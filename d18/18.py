from collections import defaultdict
from collections import deque

def getCubes():
    cubes = set()
    with open('input.in', 'r') as reader:
        line = reader.readline().strip()
        
        while line != '':
            cubes.add(tuple(map(int, line.split(','))))
            line = reader.readline().strip()

    return cubes

def sortCubes(cubes: set):
    # sort the cubes into the x, y, z coords
    xCoords = defaultdict(list)
    yCoords = defaultdict(list)
    zCoords = defaultdict(list)

    for x, y, z in cubes:
        xCoords[(y, z)].append((x, y, z))
        yCoords[(x, z)].append((x, y, z))
        zCoords[(x, y)].append((x, y, z))

    return xCoords, yCoords, zCoords

def sideCovered(coord, sameCoord, coordToCheck, coordDict):
    toMinus = 0
    if sameCoord in coordDict:
        potentialCubes = coordDict[sameCoord]

        for cube in potentialCubes:
            if abs(cube[coordToCheck] - coord[coordToCheck]) == 1:
                toMinus -= 1
    
    return toMinus

def part1(cubes: set, xCoords: dict, yCoords: dict, zCoords: dict):
    sides = 0

    for x, y, z in cubes:
        side = 6

        # see if there is any cube with the same (y, z) coords
        side += sideCovered((x, y, z), (y, z), 0, xCoords)
        # see if there is any cube with the same (x, z) coords
        side += sideCovered((x, y, z), (x, z), 1, yCoords)
        # see if there is any cube with the same (x, y) coords
        side += sideCovered((x, y, z), (x, y), 2, zCoords)

        sides += side
    
    return sides

def sidesToRemove(coord, sameCoord, coordToCheck, coordDict):
    toMinus = 0
    if sameCoord in coordDict:
        potentialCubes = coordDict[sameCoord]
        minValueForDimension = min([coord[coordToCheck] for coord in potentialCubes])
        maxValueForDimension = max([coord[coordToCheck] for coord in potentialCubes])

        # it is blocked from the left
        if coord[coordToCheck] != minValueForDimension:
            toMinus -= 1
        
        # it is blocked from the right
        if coord[coordToCheck] != maxValueForDimension:
            toMinus -= 1
    
    return toMinus

def getNeighbours(x, y, z):
    return [
        (x-1, y, z),
        (x+1, y, z),
        (x, y-1, z),
        (x, y+1, z),
        (x, y, z-1),
        (x, y, z+1)
    ]

def part2(cubes: set):
    minX = 0
    minY = 0
    minZ = 0
    maxX = 0
    maxY = 0
    maxZ = 0

    for x, y, z in cubes:
        minX = min(minX, x)
        minY = min(minY, y)
        minZ = min(minZ, z)
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        maxZ = max(maxZ, z)

    minX -= 1
    minY -= 1
    minZ -= 1
    maxX += 1
    maxY += 1
    maxZ += 1

    # stores all the points that water can reside in
    waterPoints = set()
    queue = deque()
    queue.append((minX, minY, minZ))

    while queue:
        x, y, z = queue.popleft()
        if (x, y, z) in waterPoints:
            continue
            
        waterPoints.add((x, y, z))
        neighbours = getNeighbours(x, y, z)

        # get all the potential points that can be taken up the water
        for nx, ny, nz in neighbours:
            if minX <= nx <= maxX and minY <= ny <= maxY and minZ <= nz <= maxZ:
                # only add air points since we want points that water can take up
                if (nx, ny, nz) not in cubes:
                    queue.append((nx, ny, nz))

    # get all the points that cannot be reached by water
    lavaPoints = set()
    for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):
            for z in range(minZ, maxZ + 1):
                # as long as water could not reach it, it must be lava
                # so we fill up all air gaps with lava too
                if (x, y, z) not in waterPoints:
                    lavaPoints.add((x, y, z))
                    
    return part1(lavaPoints, *sortCubes(lavaPoints))

def main():
    cubes = getCubes()
    xCoords, yCoords, zCoords = sortCubes(cubes)
    # print("part 1: {}".format(part1(cubes, xCoords, yCoords, zCoords)))
    print("part 2: {}".format(part2(cubes)))

if __name__ == "__main__":
    main()