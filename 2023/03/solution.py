# reading input
f = open('input.txt', 'r')
input = f.readlines()
lines = [i.strip() for i in input]
f.close()

# part 1

# construct the 2D grid
grid = []

for line in lines:
    grid.append([])
    for c in line:
        grid[-1].append(c)


def has_symbol_neighbor(i, j):
    neighbors = [(i-1, j), (i-1, j-1), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j), (i+1, j-1), (i+1, j+1)]
    for n in neighbors:
        try:
            if not grid[n[0]][n[1]].isnumeric() and grid[n[0]][n[1]] != ".":
                return True
        except:
            continue
    
    return False

ans = 0

for i in range(len(grid)):
    current_number = ""
    is_part = False
    for j in range(len(grid[i])):
        # keep adding numbers to current_number until number ends
        # when it ends, add to ans if applicable
        if grid[i][j].isnumeric():
            # check neighbors of number if still not identified as part
            if is_part == False:
                is_part = has_symbol_neighbor(i,j)
            current_number += grid[i][j]
        elif len(current_number) > 0 and is_part is True:
            ans += int(current_number)
            current_number = ""
            is_part = False
        else: # clear number if not next to a symbol and period identified
            current_number = ""
            is_part = False
    
    # handle if number is at end of row
    if len(current_number) > 0 and is_part is True:
        ans += int(current_number)
        current_number = ""
        is_part = False

# print(ans)


# part 2

def check_gear_neighbor(i, j):
    neighbors = [(i-1, j), (i-1, j-1), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j), (i+1, j-1), (i+1, j+1)]
    for n in neighbors:
        try:
            if grid[n[0]][n[1]] == "*":
                return (n[0], n[1])
        except:
            continue
    
    return None

gears = {}

for i in range(len(grid)):
    current_number = ""
    is_gear_num = False
    for j in range(len(grid[i])):
        # keep adding numbers to current_number until number ends
        if grid[i][j].isnumeric():
            # see if next to gear
            if is_gear_num == False:
                gear_neighbor = check_gear_neighbor(i,j)
                if gear_neighbor is not None:
                    is_gear_num = True
            current_number += grid[i][j]
        elif len(current_number) > 0 and is_gear_num is True:
            if gear_neighbor not in gears:
                gears[gear_neighbor] = []

            gears[gear_neighbor].append(int(current_number))
            current_number = ""
            is_gear_num = False
        else: # clear number if not next to a symbol and period identified
            current_number = ""
            is_gear_num = False
    
    # handle if number is at end of row
    if len(current_number) > 0 and is_gear_num is True:
        if gear_neighbor not in gears:
            gears[gear_neighbor] = []
            
        gears[gear_neighbor].append(int(current_number))
        current_number = ""
        is_gear_num = False

ans = 0

for i in gears:
    if len(gears[i]) == 2:
        ans += gears[i][0] * gears[i][1]

print(ans)