import heapq

with open('input.in', 'r') as reader:
    heap = []
    line = reader.readline()
    # currMax = 0
    currCount = 0
    while line != '':  # The EOF char is an empty string
        if line == '\n':
            heapq.heappush(heap, currCount)
            currCount = 0

            if len(heap) > 3:
                heapq.heappop(heap)
        else:
            currCount += int(line)
        line = reader.readline()

    print(sum(heap))