from io import TextIOWrapper

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

class Item:
    def __init__(self, worry: int):
        self.worry = worry
    
    def __repr__(self) -> str:
        return f'Worry: {self.worry}'

    def updateWorry(self, operation, cycleLength):
        self.worry = operation(self.worry) % cycleLength
        return self.worry

def getMonkey(line: str):
    monkeyNum = int(line.strip().split(' ')[1][0])
    return Monkey(monkeyNum)

def setMonkeyItems(line: str, monkey: Monkey):
    items = list(map(lambda x: Item((int(x))), line.strip().split(': ')[-1].split(', ')))
    monkey.items = items

def setMonkeyOperation(line: str, monkey: Monkey):
    old, opr, num = line.strip().split('= ')[-1].split(' ')

    lambdaStr = f'lambda old: old {opr} {num}'
    monkey.operation = eval(lambdaStr)

def setMonkeyTest(monkey: Monkey, reader: TextIOWrapper):
    divisibleBy = int(reader.readline().strip().split('by ')[-1])
    trueMonkey = reader.readline().strip().split('monkey ')[-1]
    falseMonkey = reader.readline().strip().split('monkey ')[-1]

    # lambdaStr = f'lambda x: {trueMonkey} if x // {divisibleBy} * {divisibleBy} == x else {falseMonkey}'
    lambdaStr = f'lambda x: {trueMonkey} if x % {divisibleBy} == 0 else {falseMonkey}'
    monkey.test = eval(lambdaStr)
    return divisibleBy

def parseInput():
    monkeys = []
    cycleLength = 1
    with open('input.in', 'r') as reader:
        while True:
            line = reader.readline()
            monkey = getMonkey(line)

            setMonkeyItems(reader.readline(), monkey)
            setMonkeyOperation(reader.readline(), monkey)
            divisibleBy = setMonkeyTest(monkey, reader)
            cycleLength *= divisibleBy
            monkeys.append(monkey)
            print(monkey)

            if reader.readline() == '':
                break
        
    print(cycleLength)
    return monkeys, cycleLength

def inspectItems(monkey: Monkey, monkeys: list[Monkey], cycleLength: int):
    inspectCount = 0
    for item in monkey.items:
        item: Item
        worry = item.updateWorry(monkey.operation, cycleLength)
        nextMonkey = monkey.test(worry)
        monkeys[nextMonkey].addItem(item)
        inspectCount += 1
    
    monkey.items = []
    
    return inspectCount

def getMonkeyBusiness(monkeys: list[Monkey], cycleLength: int):
    inspectCounts = [0] * len(monkeys)
    for i in range(10000):
        for monkey in monkeys:
            inspectCounts[monkey.num] += inspectItems(monkey, monkeys, cycleLength)

    res = [0, 0]
    print(inspectCounts)

    for count in inspectCounts:
        if count > res[0]:
            res[1] = res[0]
            res[0] = count
        elif count > res[1]:
            res[1] = count

    print(res[0] * res[1])

def run():
    monkeys, cycleLength = parseInput()
    getMonkeyBusiness(monkeys, cycleLength)

if __name__ == "__main__":
    run()