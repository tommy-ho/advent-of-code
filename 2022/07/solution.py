# reading input
f = open('input.txt', 'r')
input = f.readlines()
input = [i.strip() for i in input]
f.close()

# part 1

class Item:
    def __init__(self, name, type, size=0, parent=None):
        self.name = name
        self.type = type
        self.size = size
        self.parent = parent
        self.children = {}

    def add_child(self, item):
        self.children.append(item)


current = None
root = None

for line in input:
    line = line.split(' ')
    if line[0] == '$':
        cmd = line[1]
        if cmd == 'cd':
            if current is None:
                current = Item(line[2], 'dir')
                root = current
            elif line[2] == '..':
                current = current.parent
            elif line[2] == '/':
                current = root
            else:
                current = current.children[line[2]]
        # elif cmd == 'ls':
            #  do nothing because it will get handled at next iteration
    elif line[0] == 'dir': # add dir as a child to current
        current.children[line[1]] = Item(current.name + '/' + line[1], 'dir', parent=current)
    else: # it's a file
        current.children[line[1]] = Item(current.name + '/' + line[1], 'file', size=int(line[0]), parent=current)


print()

# use BFS to find the size of all directories
dir_sizes = {}
q = []
q.append(root)
while (len(q) > 0):
    item = q.pop(0)

    if item.type == 'dir':
        dir_sizes[item.name] = item.size

    parent = item.parent

    while parent is not None:
        dir_sizes[parent.name] += item.size
        parent = parent.parent

    for child in item.children:
        c = item.children[child]
        q.append(c)
    
ans = 0
for dir in dir_sizes:
    if dir_sizes[dir] <= 100000:
        ans += dir_sizes[dir]

print(ans)

# part 2

used = 0

q = []
q.append(root)
while (len(q) > 0):
    item = q.pop(0)

    if item.type == 'file':
        used += item.size

    parent = item.parent

    for child in item.children:
        c = item.children[child]
        q.append(c)

total = 70000000
required = 30000000
need = required - (total - used)
smallest = None

for dir in dir_sizes:
    if dir_sizes[dir] >= need:
        if smallest is None or dir_sizes[dir] < smallest[1]:
            smallest = (dir, dir_sizes[dir])

print(smallest)