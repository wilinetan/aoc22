A_CODE = ord('A')
Z_CODE = ord('Z')
a_CODE = ord('a')

with open('input.in', 'r') as reader:
    line = reader.readline().strip()
    total = 0
    count = 0
    chars = set()
    while line != '':
        if count == 0:
            chars = set(line)
        else:
            newSet = set()
            for c in line:
                if c in chars:
                    newSet.add(c)
            chars = newSet

        count = (count + 1) % 3
        if count == 0:
            for char in chars:
                code = ord(char)
                if code <= Z_CODE:
                    total += code - A_CODE + 27
                else:
                    total += code - a_CODE + 1
            chars.clear()

        line = reader.readline().strip()
    
    print(total)