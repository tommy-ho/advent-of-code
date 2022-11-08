# reading input
f = open('input.txt', 'r')
instr = f.read()
f.close()

# part 1

dict = {(0,0): 1}
x = 0
y = 0


for dir in instr:
    if dir == '^':
        y += 1
    elif dir == '>':
        x += 1
    elif dir == 'v':
        y -= 1
    elif dir == '<':
        x -= 1
    
    if (x,y) not in dict:
        dict[(x,y)] = 1
    else:
        dict[(x,y)] += 1

print(len(dict))

# part 2

dict = {(0,0): 2}
x1 = 0
y1 = 0
x2 = 0
y2 = 0

santas_turn = True

for dir in instr:
    x = x1 if santas_turn else x2
    y = y1 if santas_turn else y2

    if dir == '^':
        y += 1
    elif dir == '>':
        x += 1
    elif dir == 'v':
        y -= 1
    elif dir == '<':
        x -= 1

    if (x,y) not in dict:
        dict[(x,y)] = 1
    else:
        dict[(x,y)] += 1
    
    if santas_turn:
        x1 = x
        y1 = y
    else:
        x2 = x
        y2 = y

    santas_turn = not santas_turn
    
print(len(dict))
