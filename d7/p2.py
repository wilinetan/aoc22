class Node:
    def __init__(self, size, path, isDir):
        self.size = size
        self.parent = None
        self.childDirs = []
        self.childFiles = []
        self.path = path
        self.isDir = isDir

def parseLine(line: str):
    arr = line.split(' ')
    return arr

def getDirSizes(rootNode: Node):
    dirs = set()
    def dfs(node: Node):
        size = node.size
        for child in node.childDirs:
            size += dfs(child)
        
        node.size = size

        if node.isDir:
            dirs.add(node)
        return size

    dfs(rootNode)
    return dirs

def getPath(currDir: Node, dirName: str):
    return '{}/{}'.format(currDir.path if currDir.path != '/' else '', dirName)

def getSizeSum():
    CD = 'cd'
    LS = 'ls'
    PARENT_DIR = '..'
    ROOT_DIR = '/'
    CMD = '$'
    DISK_SPACE = 70000000
    REQUIRED_UNUSED_SPACE = 30000000
    rootNode = Node(0, '/', True)

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
                        node = Node(0, path, True)
                        currDir.childDirs.append(node)
                    else:
                        node = Node(int(fileType), path, False)
                        currDir.childFiles.append(node)

                    node.parent = currDir
                    tree[path] = node
                    size += node.size
                    line = reader.readline().strip()
                currDir.size = size
                continue
        
        dirs = getDirSizes(rootNode)
        currUsed = rootNode.size
        currUnused = DISK_SPACE - currUsed
        spaceRequired = REQUIRED_UNUSED_SPACE - currUnused
        if spaceRequired <= 0:
            print("no need to delete")
        
        res = currUsed
        for dir in dirs:
            if dir.size >= spaceRequired and dir.size < res:
                res = dir.size
        print(res)
        

if __name__ == "__main__":
    getSizeSum()