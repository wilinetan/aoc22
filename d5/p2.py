from collections import deque

def getStackIndex(index):
    return index // 4

def parseAction(line: str):
    fromIndex = line.index('from')
    toIndex = line.index('to')
    numCrates = int(line[5:fromIndex - 1])
    fromStack = int(line[fromIndex+5:toIndex - 1])
    toStack = int(line[toIndex+3])
    return numCrates, fromStack, toStack

def moveCrates(numCrates, fromStack, toStack, stacks):
    temp = []
    for i in range(numCrates):
        temp.append(stacks[fromStack - 1].popleft())
    
    for i in range(numCrates):
        stacks[toStack - 1].appendleft(temp.pop())

def parse():
    with open('input.in', 'r') as reader:
        # print(reader.readlines())
        line = reader.readline()
        length = len(line)
        print(length)
        stacks = [deque() for _ in range(length // 4)]
        while '1' not in line:
            for i in range(0, length, 4):
                if line[i] == '[':
                    stacks[getStackIndex(i)].append(line[i+1:i+2])
            line = reader.readline()
        print(stacks)
        # get the empty line
        print(reader.readline())
        
        line = reader.readline()

        while line != '':
            numCrates, fromStack, toStack = parseAction(line)

            moveCrates(numCrates, fromStack, toStack, stacks)

            line = reader.readline()

        print(stacks)
        print(''.join([stack.popleft() for stack in stacks if stack]))


if __name__ == "__main__":
    parse()