# A: rock, B: paper, C: scissor
# X: lose, Y: draw, Z: win
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won
scoring = {
    'A': {
        'X': 3,
        'Y': 4,
        'Z': 8
    },
    'B': {
        'X': 1,
        'Y': 5,
        'Z': 9
    },
    'C': {
        'X': 2,
        'Y': 6,
        'Z': 7
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