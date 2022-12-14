# reading input
f = open('input.txt', 'r')
input = f.readlines()
instructions = [i.strip() for i in input]
f.close()


# part 1

H = [0,0]
T = [0,0]
visited = set()
visited.add((T[0], T[1]))

# follow the instructions

for instr in instructions:
    dir, steps = instr.split(' ')
    steps = int(steps)

    while steps > 0:
        if dir == 'U':
            H[0] += 1
        elif dir == 'D':
            H[0] -= 1
        elif dir == 'R':
            H[1] += 1
        elif dir == 'L':
            H[1] -= 1

        if abs(H[0] - T[0]) == 2 and abs(H[1] - T[1]) == 1:
            T[0] = (T[0] + H[0]) / 2
            T[1] = H[1]
        elif abs(H[0] - T[0]) == 1 and abs(H[1] - T[1]) == 2:
            T[0] = H[0]
            T[1] = (T[1] + H[1]) / 2
        elif abs(H[0] - T[0]) > 1:
            T[0] = (T[0] + H[0]) / 2
        elif abs(H[1] - T[1]) > 1:
            T[1] = (T[1] + H[1]) / 2

        visited.add((int(T[0]), int(T[1])))
        steps -= 1

        # outputs = []
        # for i in range(6):
        #     line = ''
        #     for j in range(6):
        #         if [i,j] == H:
        #             line += 'H'
        #         elif [i,j] == T:
        #             line += 'T'
        #         else:
        #             line += '.'
        #     outputs.append(line)
        
        # while len(outputs) > 0:
        #     print(outputs.pop())
        # print()
    

print(len(visited))


# part 2

knots = []
for i in range(10):
    knots.append([0, 0])

visited = set()
visited.add((knots[0][0], knots[0][1]))

# follow the instructions

for instr in instructions:
    dir, steps = instr.split(' ')
    steps = int(steps)

    while steps > 0:
        # move head knot
        if dir == 'U':
            knots[0][0] += 1
        elif dir == 'D':
            knots[0][0] -= 1
        elif dir == 'R':
            knots[0][1] += 1
        elif dir == 'L':
            knots[0][1] -= 1
        
        # update all tail knots
        for i in range(1, 10):
            H = knots[i-1]
            T = knots[i]
            # 1 extra scenario where rope is pulled diagonally
            if abs(H[0] - T[0]) == 2 and abs(H[1] - T[1]) == 2:
                T[0] = (T[0] + H[0]) / 2
                T[1] = (T[1] + H[1]) / 2
            elif abs(H[0] - T[0]) == 2 and abs(H[1] - T[1]) == 1:
                T[0] = (T[0] + H[0]) / 2
                T[1] = H[1]
            elif abs(H[0] - T[0]) == 1 and abs(H[1] - T[1]) == 2:
                T[0] = H[0]
                T[1] = (T[1] + H[1]) / 2
            elif abs(H[0] - T[0]) > 1:
                T[0] = (T[0] + H[0]) / 2
            elif abs(H[1] - T[1]) > 1:
                T[1] = (T[1] + H[1]) / 2

        visited.add((int(T[0]), int(T[1])))
        
        steps -= 1

        # outputs = []
        # for i in range(35):
        #     line = ''
        #     for j in range(35):
        #         for k in range(len(knots)):
        #             if knots[k] == [i,j]:
        #                 line += str(k)
        #                 break
        #         else:
        #             line += '.'
        #     outputs.append(line)
        
        # while len(outputs) > 0:
        #     print(outputs.pop())
        # print()
    
print(len(visited))