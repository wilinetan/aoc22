def parseLine(line: str):
    return line.strip().split(' ')

def updateCrt(crt: list, sprite: int, cycle: int):
    WIDTH = 40
    
    cycle -= 1

    row = cycle // WIDTH
    col = cycle % WIDTH

    if col == sprite or col + 1 == sprite or col - 1 == sprite:
        crt[row][col] = '#'
    else:
        crt[row][col] = '.'

def printCrt(crt):
    for i in range(len(crt)):
        print(''.join(crt[i]))

def run():
    NOOP = 'noop'
    currCycle = 1
    sprite = 1

    crt = [[''] * 40 for _ in range(6)]

    with open('input.in', 'r') as reader:
        line = reader.readline()

        while line != '':
            arr = parseLine(line)

            if arr[0] == NOOP:
                updateCrt(crt, sprite, currCycle)
                currCycle += 1
            else:
                updateCrt(crt, sprite, currCycle)
                currCycle += 1
                updateCrt(crt, sprite, currCycle)
                currCycle += 1
                sprite += int(arr[1])
            
            line = reader.readline()

    printCrt(crt)

if __name__ == "__main__":
    run()