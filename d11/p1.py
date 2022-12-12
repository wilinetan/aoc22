from io import TextIOWrapper
import inspect

class Monkey:
    def __init__(self, num: int):
        self.num = num
        self.items = []
        self.operation = None
        self.test = None

    def addItem(self, item: int):
        self.items.append(item)

    def __repr__(self) -> str:
        return f'num: {self.num}, items: {self.items}, operation: {self.operation}, test: {self.test}'

def getMonkey(line: str):
    monkeyNum = int(line.strip().split(' ')[1][0])
    return Monkey(monkeyNum)

def setMonkeyItems(line: str, monkey: Monkey):
    items = list(map(int, line.strip().split(': ')[-1].split(', ')))
    monkey.items = items
    return monkey

def setMonkeyOperation(line: str, monkey: Monkey):
    old, opr, num = line.strip().split('= ')[-1].split(' ')

    lambdaStr = f'lambda old: old {opr} {num}'
    monkey.operation = eval(lambdaStr)
    return monkey

def setMonkeyTest(monkey: Monkey, reader: TextIOWrapper):
    divisibleBy = reader.readline().strip().split('by ')[-1]
    trueMonkey = reader.readline().strip().split('monkey ')[-1]
    falseMonkey = reader.readline().strip().split('monkey ')[-1]

    # lambdaStr = f'lambda x: {trueMonkey} if x % {divisibleBy} == 0 else {falseMonkey}'
    lambdaStr = f'lambda x: {trueMonkey} if x // {divisibleBy} * {divisibleBy} == x else {falseMonkey}'
    monkey.test = eval(lambdaStr)
    return monkey

def parseInput():
    monkeys = []
    with open('input.in', 'r') as reader:
        while True:
            line = reader.readline()
            monkey = getMonkey(line)

            setMonkeyItems(reader.readline(), monkey)
            setMonkeyOperation(reader.readline(), monkey)
            setMonkeyTest(monkey, reader)
            monkeys.append(monkey)

            if reader.readline() == '':
                break

    return monkeys

def inspectItems(monkey: Monkey, monkeys: list[Monkey]):
    inspectCount = 0
    for item in monkey.items:
        worryLvl = monkey.operation(item) // 3
        nextMonkey = monkey.test(worryLvl)
        monkeys[nextMonkey].addItem(worryLvl)
        inspectCount += 1
    
    monkey.items = []
    
    return inspectCount

def getMonkeyBusiness(monkeys: list[Monkey]):
    inspectCounts = [0] * len(monkeys)
    for _ in range(20):
        for monkey in monkeys:
            inspectCounts[monkey.num] += inspectItems(monkey, monkeys)

    res = [0, 0]

    for count in inspectCounts:
        if count > res[0]:
            res[1] = res[0]
            res[0] = count
        elif count > res[1]:
            res[1] = count

    print(res[0] * res[1])


def run():
    monkeys = parseInput()
    getMonkeyBusiness(monkeys)

if __name__ == "__main__":
    run()