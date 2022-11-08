# part 1
f = open('input.txt', 'r')
instr = f.read()
f.close()
floor = 0

for x in instr:
    if x == '(':
        floor += 1
    else:
        floor -= 1

print(floor)


# part 2
floor = 0
ans = 0

for i in range(len(instr)):
    if instr[i] == '(':
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        ans = i + 1
        break

print(ans)
