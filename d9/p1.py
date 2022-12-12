def parseLine(line: str):
    return line.strip().split(' ')

RIGHT = 'R'
UP = 'U'
LEFT = 'L'
DOWN = 'D'

dirs = {
    'R': [1, 0],
    'U': [0, 1],
    'L': [-1, 0],
    'D': [0, -1]
}

def move(dir: str, steps: int, head: tuple, tail: tuple, res: set):
    for i in range(steps):
        head[0] += dirs[dir][0]
        head[1] += dirs[dir][1]

        # check if tail is touching head
        # same row
        if head[0] == tail[0]:
            if abs(head[1] - tail[1]) > 1:
                # need to move tail
                tail[1] += 1 if head[1] > tail[1] else -1
        # same col
        elif head[1] == tail[1]:
            if abs(head[0] - tail[0]) > 1:
                tail[0] += 1 if head[0] > tail[0] else -1
        
        # not same row or col
        else:
            # not directly adjacent
            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                tail[0] += 1 if head[0] > tail[0] else -1
                tail[1] += 1 if head[1] > tail[1] else -1
        
        res.add(tuple(tail))
        
    

def run():
    # [row, col]
    head = [0, 0]
    tail = [0, 0]
    res = set()

    res.add(tuple(tail))
    
    with open('input.in', 'r') as reader:
        line = reader.readline()

        while line != '':
            dir, steps = parseLine(line)
            move(dir, int(steps), head, tail, res)
            line = reader.readline()

    print(len(res))

if __name__ == "__main__":
    run()