# A: rock, B: paper, C: scissor
# X: rock, Y: paper, Z: scissor
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won
scoring = {
    'A': {
        'X': 4,
        'Y': 8,
        'Z': 3
    },
    'B': {
        'X': 1,
        'Y': 5,
        'Z': 9
    },
    'C': {
        'X': 7,
        'Y': 2,
        'Z': 6
    }
}

with open('input.in', 'r') as reader:
    line = reader.readline()
    total = 0
    while line != '':
        opp, me = line.strip().split(' ')
        total += scoring[opp][me]
        line = reader.readline()
    
    print(total)