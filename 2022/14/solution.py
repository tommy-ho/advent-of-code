from sys import maxsize

# reading input
f = open('input.txt', 'r')
input = f.readlines()
lines = [i.strip() for i in input]
f.close()

# construct the grid using dict to capture each coordinate in grid
grid = {}
max_depth = -1 * maxsize

for line in lines:
    coords = line.split(' -> ')
    start_x, start_y = coords[0].split(',')
    start_x = int(start_x)
    start_y = int(start_y)

    for i in range(1,len(coords)):
        end_x, end_y = coords[i].split(',')
        end_x = int(end_x)
        end_y = int(end_y)
        
        # 4 possible ways to construct the rocks
        if start_x < end_x:
            while start_x <= end_x:
                grid[start_x, start_y] = '#'
                start_x += 1
        elif start_y < end_y:
            while start_y <= end_y:
                grid[start_x, start_y] = '#'
                start_y += 1
        elif start_x > end_x:
            while start_x >= end_x:
                grid[start_x, start_y] = '#'
                start_x -= 1
        elif start_y > end_y:
            while start_y >= end_y:
                grid[start_x, start_y] = '#'
                start_y -= 1
    
        start_x = end_x
        start_y = end_y
        # capture depth of lowest rock structure
        max_depth = max(max_depth, end_y)


grid2 = grid.copy() # copying grid for part 2

# part 1

max_depth_reached = False
source = (500,0)
count = 0

while True: # until sand start falling into the abyss
    current = source

    while True: # sand keeps falling if possible
        if current[1] >= max_depth:
            max_depth_reached = True
            break

        if (current[0], current[1]+1) not in grid:
            current = (current[0], current[1]+1)
            continue
        
        if (current[0]-1, current[1]+1) not in grid:
            current = (current[0]-1, current[1]+1)
            continue
        
        if (current[0]+1, current[1]+1) not in grid:
            current = (current[0]+1, current[1]+1)
            continue
        
        break # no longer falling
    
    
    if max_depth_reached:
        break

    grid[current] = 'o' # sand settled
    count += 1

print(count)


# part 2

max_depth += 2
source = (500,0)
count = 0

while True: # until sand blocks the source
    current = source

    while True: # sand keeps falling if possible
        if current[1] == max_depth-1:
            break

        if (current[0], current[1]+1) not in grid2:
            current = (current[0], current[1]+1)
            continue
        
        if (current[0]-1, current[1]+1) not in grid2:
            current = (current[0]-1, current[1]+1)
            continue
        
        if (current[0]+1, current[1]+1) not in grid2:
            current = (current[0]+1, current[1]+1)
            continue
        
        break # no longer falling
    

    grid2[current] = 'o' # sand settled
    count += 1

    if source in grid2:
        break

print(count)