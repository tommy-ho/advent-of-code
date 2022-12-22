# reading input
f = open('input.txt', 'r')
input = f.readlines()
lines = [i.strip() for i in input]
f.close()

# part 1


# 1 means in order
# -1 means not in order
# 0 means not determined
def compare(left, right):
    if type(left) is int and type(right) is int:
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1
    elif type(left) is list and type(right) is list:
        for k in range(min(len(left), len(right))):
            res = compare(left[k], right[k])
            if res != 0:
                return res
        if len(left) < len(right): # left side ran out of items
            return 1
        elif len(left) > len(right): # right side ran out
            return -1

        return 0 # because no conclusion found on this level
    else:
        left = [left] if type(left) is int else left
        right = [right] if type(right) is int else right
        return compare(left, right)

in_order = []

# iterate over pairs of packets
for i in range(0, len(lines), 3):
    p1, p2 = None, None
    exec('p1 = ' + lines[i])
    exec('p2 = ' + lines[i+1])
    done = False

    if compare(p1, p2) == 1:
        in_order.append(True)
    else:
        in_order.append(False)


ans = 0
for i in range(len(in_order)):
    if in_order[i]:
        ans += i+1

print(ans)

# part 2 - implement a sorting algo using the compare func

# get rid of blank lines
packets = []

for i in range(len(lines)):
    if lines[i] != '':
        packet = None
        exec('packet = ' + lines[i])
        packets.append(packet)

# add divider packets
packets.append([[2]])
packets.append([[6]])


# bubble sort
for i in range(len(packets)):
    for j in range(len(packets)-1):
        if compare(packets[j], packets[j+1]) == -1:
            packets[j], packets[j+1] = packets[j+1], packets[j]

ans = 1

for i in range(len(packets)):
    if packets[i] in ([[2]], [[6]]):
        ans *= i+1

print(ans)