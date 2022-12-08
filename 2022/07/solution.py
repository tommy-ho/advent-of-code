# reading input
f = open('input.txt', 'r')
input = f.readlines()
input = [i.strip() for i in input]
f.close()

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
    # if current is not None:
    #     print(f'currently in {current.name}')
    # print(line)
    line = line.split(' ')
    if line[0] == '$':
        cmd = line[1]
        if cmd == 'cd':
            if current is None:
                current = Item(line[2], 'dir')
                root = current
            elif line[2] == '..':
                current = current.parent
                # print(f'moving up dir to {current.name}')
            elif line[2] == '/':
                current = root
            else:
                current = current.children[line[2]]
        # elif cmd == 'ls':
            # continue -- do nothing because it will get handled at next iteration
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

    # try:
    #     print(f'{item.name} of size {item.size} with parent {item.parent.name}')
    # except:
    #     print()

    if item.type == 'dir':
        dir_sizes[item.name] = item.size

    parent = item.parent

    while parent is not None:
        # print(f'updating {parent.name} by adding {item.size}')
        dir_sizes[parent.name] += item.size
        parent = parent.parent

    for child in item.children:
        c = item.children[child]
        q.append(c)
    

# print(dir_sizes)

ans = 0
for dir in dir_sizes:
    if dir_sizes[dir] <= 100000:
        ans += dir_sizes[dir]

print(ans)