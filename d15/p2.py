class Sensor:
    def __init__(self, coord, dist, beacon):
        self.coord = coord
        self.dist = dist
        self.beacon = beacon

    def __str__(self) -> str:
        return f'coord: {self.coord}, dist: {self.dist}, beacon: {self.beacon}'

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

def getSensors() -> list[Sensor]:
    sensors = []

    with open('input.in', 'r') as reader:
        line = reader.readline()

        while line != '':
            sensorCoord, beaconCoord = parseLine(line)

            dist = getManhattenDist(sensorCoord, beaconCoord)
            sensors.append(Sensor(sensorCoord, dist, beaconCoord))
    
            line = reader.readline()

    return sensors

def getTuningFreq(sensors: list[Sensor]):
    MAX = 4000000

    for y in range(MAX):
        x = 0
        while x <= MAX:
            # print(x,y)
            isChanged = False
            for sensor in sensors:
                d = getManhattenDist((x, y), sensor.coord)
                # sensor can see this so update x value
                if d <= sensor.dist:
                    dx = sensor.dist - abs(y - sensor.coord[1])
                    rightmost = sensor.coord[0] + dx + 1

                    if rightmost <= x:
                        continue
                    
                    x = rightmost
                    isChanged = True
                    break

            # we found a location where no sensor can see it
            if not isChanged:
                return x * MAX + y
    
    return -1

def run():
    sensors = getSensors()
    # [print(sensor) for sensor in sensors]
    print(getTuningFreq(sensors))

if __name__ == "__main__":
    run()