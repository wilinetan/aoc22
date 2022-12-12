from collections import deque, defaultdict

def getInput():
    with open('input.in', 'r') as reader:
        line = reader.readline()
        return line

def parseInput(line):
    charCount = defaultdict(int)
    marker = deque()

    numUnique = 0

    i = 0

    while i < len(line):
        marker.append(line[i])
        charCount[line[i]] += 1

        if charCount[line[i]] == 1:
            numUnique += 1

        if len(marker) == 4:
            if numUnique == 4:
                return i + 1
            
            front = marker.popleft()
            charCount[front] -= 1

            if charCount[front] == 0:
                numUnique -= 1
        
        i += 1


def getMarker():
    line = getInput()
    print(parseInput(line))

if __name__ == "__main__":
    getMarker()