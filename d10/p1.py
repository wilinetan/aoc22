def parseLine(line: str):
    return line.strip().split(' ')

def run():
    NOOP = 'noop'
    currCycle = 1
    currValue = 1
    cycleCount = 19
    res = 0

    with open('input.in', 'r') as reader:
        line = reader.readline()

        while line != '':
            arr = parseLine(line)

            if arr[0] == NOOP:
                currCycle += 1
            else:
                currCycle += 2
                currValue += int(arr[1])
            
            if currCycle >= cycleCount:
                print(currCycle, currValue)
                res += (cycleCount + 1) * currValue
                cycleCount += 40
            
            line = reader.readline()
    
    print(res)

if __name__ == "__main__":
    run()