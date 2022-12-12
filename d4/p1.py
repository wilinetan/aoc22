def getCount():
    count = 0
    with open('input.in', 'r') as reader:
        line = reader.readline().strip()
        while line != '':
            w1, w2 = line.split(',')
            if isOverlap(w1, w2):
                count += 1

            line = reader.readline().strip()

    return count

def isOverlap(w1, w2):
    start1, end1 = map(int, w1.split('-'))
    start2, end2 = map(int, w2.split('-'))
    
    return (start2 >= start1 and end2 <= end1) or (start1 >= start2 and end1 <= end2)


if __name__ == "__main__":
    print(getCount())