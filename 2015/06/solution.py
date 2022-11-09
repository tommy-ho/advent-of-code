# reading input
f = open('input.txt', 'r')
instructions = f.readlines()
f.close()

# part 1

grid = [[0 for i in range(1000)] for j in range(1000)]

for x in instructions:
    split = x.split(' ')

    if 'toggle' in x:
        start = split[1]
        end = split[3]
    else:
        start = split[2]
        end = split[4]

    start_split = start.split(',')
    end_split = end.split(',')

    start_x = int(start_split[0])
    start_y = int(start_split[1])
    end_x = int(end_split[0])
    end_y = int(end_split[1])

    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            if 'on' in x:
                grid[i][j] = 1
            elif 'off' in x:
                grid[i][j] = 0
            else:
                grid[i][j] = 1 - grid[i][j]
    
lit = 0
for i in grid:
    for j in i:
        lit += j

print(lit)

# part 2

grid = [[0 for i in range(1000)] for j in range(1000)]

for x in instructions:
    split = x.split(' ')

    if 'toggle' in x:
        start = split[1]
        end = split[3]
    else:
        start = split[2]
        end = split[4]

    start_split = start.split(',')
    end_split = end.split(',')

    start_x = int(start_split[0])
    start_y = int(start_split[1])
    end_x = int(end_split[0])
    end_y = int(end_split[1])

    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            if 'on' in x:
                grid[i][j] += 1
            elif 'off' in x:
                grid[i][j] = max(grid[i][j] - 1, 0)
            else:
                grid[i][j] += 2
    
brightness = 0
for i in grid:
    for j in i:
        brightness += j

print(brightness)