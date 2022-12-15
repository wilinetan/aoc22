def parseLine(line: str):
    return eval(line.strip())

def isCorrectOrder(l1: list, l2: list):
    i = 0

    while i < len(l1) and i < len(l2):
        if type(l1[i]) is int and type(l2[i]) is int:
            if l1[i] == l2[i]:
                i += 1
                continue
            else:
                return l1[i] - l2[i]
        else:
            # 2 cases
            # 1. both lists
            # 2. one is int, one is list so convert both to lists
            l1[i] = [l1[i]] if type(l1[i]) is int else l1[i]
            l2[i] = [l2[i]] if type(l2[i]) is int else l2[i]

            order = isCorrectOrder(l1[i], l2[i])

            if isCorrectOrder(l1[i], l2[i]) == 0:
                i += 1
                continue
            return order

    return len(l1) - len(l2)


def getSum():
    index = 1
    res = 0
    with open('input.in', 'r') as reader:
        while True:
            line1 = reader.readline()
            list1 = parseLine(line1)

            line2 = reader.readline()
            list2 = parseLine(line2)

            order = isCorrectOrder(list1, list2)
            assert order != 0

            if order < 0:
                print(f'to add: {index}')
                res += index
            
            if reader.readline() == '':
                break
            
            index += 1
    
    return res

def run():
    res = getSum()
    print(res)

if __name__ == "__main__":
    run()