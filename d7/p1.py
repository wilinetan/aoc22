class Node:
    def __init__(self, name, size, path):
        self.name = name
        self.size = size
        self.parent = None
        self.childDirs = []
        self.childFiles = []
        self.path = path

def parseLine(line: str):
    arr = line.split(' ')
    return arr

def getSizes(rootNode: Node):
    MAX_SIZE = 100000
    res = 0
    def dfs(node):
        nonlocal res
        size = node.size
        for child in node.childDirs:
            size += dfs(child)
        
        node.size = size
        if size <= MAX_SIZE:
            res += size
        return size

    dfs(rootNode)
    return res

def getPath(currDir: Node, dirName: str):
    return '{}/{}'.format(currDir.path if currDir.path != '/' else '', dirName)

def getSizeSum():
    CD = 'cd'
    LS = 'ls'
    PARENT_DIR = '..'
    ROOT_DIR = '/'
    CMD = '$'
    rootNode = Node('/', 0, '/')

    # path-node map
    tree = {'/': rootNode}
    currDir = rootNode

    with open('input.in', 'r') as reader:
        line = reader.readline().strip()

        while line != '':
            arr = parseLine(line)
            if arr[1] == CD:
                dirName = arr[2]
                if dirName == PARENT_DIR:
                    currDir = currDir.parent
                elif dirName == ROOT_DIR:
                    currDir = rootNode
                else:
                    currDir = tree[getPath(currDir, dirName)]
                line = reader.readline().strip()
            else:
                # ls command
                line = reader.readline().strip()
                size = 0
                while line != '' and line[0] != CMD:
                    fileType, name = line.split(' ')
                    node = None
                    path = getPath(currDir, name)
                    if fileType == 'dir':
                        node = Node(name, 0, path)
                        currDir.childDirs.append(node)
                    else:
                        node = Node(name, int(fileType), path)
                        currDir.childFiles.append(node)

                    node.parent = currDir
                    tree[path] = node
                    size += node.size
                    line = reader.readline().strip()
                currDir.size = size
                continue
        
        print(getSizes(rootNode))
        

if __name__ == "__main__":
    getSizeSum()