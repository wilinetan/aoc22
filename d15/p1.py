def getCoord(line: str):
    xPart, yPart = line.split(', ')
    xCoord = int(xPart.split('=')[-1])
    yCoord = int(yPart.split('=')[-1])

    return (xCoord, yCoord)

def parseLine(line: str):
    sensor, beacon = line.strip().split(': ')

    sensorCoord = getCoord(sensor)
    beaconCoord = getCoord(beacon)

    return sensorCoord, beaconCoord

def getManhattenDist(p1: tuple, p2: tuple):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def getGrid():
    Y_COORD = 2000000
    xCoords = set()
    beaconAtYCoord = set()

    with open('input.in', 'r') as reader:
        line = reader.readline()

        while line != '':
            sensorCoord, beaconCoord = parseLine(line)
            if beaconCoord[1] == Y_COORD:
                beaconAtYCoord.add(beaconCoord[0])

            dist = getManhattenDist(sensorCoord, beaconCoord)

            distToYCoord = abs(sensorCoord[1] - Y_COORD)
            xCoordDiff = dist - distToYCoord

            if xCoordDiff > 0:
                xCoord1 = xCoordDiff + sensorCoord[0]
                xCoord2 = -xCoordDiff + sensorCoord[0]

                for i in range(xCoord2, xCoord1+1):
                    if i in beaconAtYCoord:
                        continue
                    xCoords.add(i)
    
            line = reader.readline()
        
        print(len(xCoords))

def run():
    getGrid()

if __name__ == "__main__":
    run()