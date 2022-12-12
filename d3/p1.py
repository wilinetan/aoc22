A_CODE = ord('A')
Z_CODE = ord('Z')
a_CODE = ord('a')

with open('input.in', 'r') as reader:
    line = reader.readline().strip()
    total = 0
    while line != '':
        chars = set()
        for i in range(len(line)):
            if i < len(line) / 2:
                chars.add(line[i])
            else:
                if line[i] in chars:
                    code = ord(line[i])
                    if code <= Z_CODE:
                        total += code - A_CODE + 27
                    else:
                        total += code - a_CODE + 1
                    break

        line = reader.readline().strip()
    
    print(total)