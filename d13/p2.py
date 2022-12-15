class Packet:
    def __init__(self, data: list):
        self.data = data

    def __lt__(self, other):
        return getOrder(self.data, other.data) < 0

    def __str__(self) -> str:
        return ''.join(str(x) for x in self.data)

def parseLine(line: str):
    return eval(line.strip())

def getOrder(l1: list, l2: list):
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

            order = getOrder(l1[i], l2[i])

            if getOrder(l1[i], l2[i]) == 0:
                i += 1
                continue
            return order

    return len(l1) - len(l2)

def getPackets():
    packets = []
    with open('input.in', 'r') as reader:
        line = reader.readline()

        while line != '':
            if line != '\n':
                packets.append(Packet(parseLine(line)))
            
            line = reader.readline()

    return packets

def getDecoderKey(packets: list):
    divider1 = Packet([[2]])
    divider2 = Packet([[6]])

    packets.extend([divider1, divider2])
    packets.sort()
    
    res = 1

    for i in range(len(packets)):
        if packets[i] is divider1 or packets[i] is divider2:
            res *= (i + 1)

    print(res)

def run():
    packets = getPackets()
    getDecoderKey(packets)

if __name__ == "__main__":
    run()