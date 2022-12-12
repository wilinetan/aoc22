def parseLine(line: str):
    return line.strip().split(' ')

dirs = {
    'R': [1, 0],
    'U': [0, 1],
    'L': [-1, 0],
    'D': [0, -1]
}

def move(dir: str, steps: int, rope: list, res: set):
    for _ in range(steps):
        rope[0][0] += dirs[dir][0]
        rope[0][1] += dirs[dir][1]

        for i in range(1, 10):
            prevKnot = rope[i-1]
            currKnot = rope[i]
            # same row
            if prevKnot[0] == currKnot[0]:
                if abs(prevKnot[1] - currKnot[1]) > 1:
                    currKnot[1] += 1 if prevKnot[1] > currKnot[1] else -1

            # same col
            elif prevKnot[1] == currKnot[1]:
                if abs(prevKnot[0] - currKnot[0]) > 1:
                    currKnot[0] += 1 if prevKnot[0] > currKnot[0] else -1
            
            # not same row or col
            else:
                # not directly adjacent
                if abs(prevKnot[0] - currKnot[0]) > 1 or abs(prevKnot[1] - currKnot[1]) > 1:
                    currKnot[0] += 1 if prevKnot[0] > currKnot[0] else -1
                    currKnot[1] += 1 if prevKnot[1] > currKnot[1] else -1
        
        res.add(tuple(rope[-1]))

def run():
    rope = [[0, 0] for _ in range(10)]
    res = set()

    res.add(tuple(rope[-1]))
    
    with open('input.in', 'r') as reader:
        line = reader.readline()

        while line != '':
            dir, steps = parseLine(line)
            move(dir, int(steps), rope, res)
            line = reader.readline()

    print(len(res))

if __name__ == "__main__":
    run()