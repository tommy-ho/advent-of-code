# reading input
f = open('input.txt', 'r')
input = f.readlines()
input = [i.strip() for i in input]
f.close()

# part 1

grid = []
visible = []

for i in input:
    grid.append([])
    visible.append([])
    for j in i:
        grid[-1].append(j)
        visible[-1].append(False)


# set the corners first
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[i])-1: # corners
            visible[i][j] = True


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[i])-1: # corners
            continue

        # look left
        jj = j - 1
        while grid[i][j] > grid[i][jj]:
            if jj == 0:
                visible[i][j] = True
                break
            jj -= 1


        # look up
        ii = i - 1
        while grid[i][j] > grid[ii][j]:
            if ii == 0:
                visible[i][j] = True
                break
            ii -= 1

        # start from end

        # look down
        x = len(grid)-i-1
        y = len(grid[i])-j-1
        
        xx = x + 1
        while grid[x][y] > grid[xx][y]:
            if xx == len(grid)-1:
                visible[x][y] = True
                break
            xx += 1

        # look right
        yy = y + 1
        while grid[x][y] > grid[x][yy]:
            if yy == len(grid[i])-1:
                visible[x][y] = True
                break
            yy += 1
        


ans = 0
for i in visible:
    for j in i:
        if j is True:
            ans += 1

print(ans)

# part 2

max_score = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        # look left
        left = 0
        jj = j
        while jj > 0:
            jj -= 1
            if grid[i][j] > grid[i][jj]:
                left += 1
            else:
                left += 1
                break

        # look up
        up = 0
        ii = i
        while ii > 0:
            ii -= 1
            if grid[i][j] > grid[ii][j]:
                up += 1
            else:
                up += 1
                break

        # look right
        right = 0
        jj = j
        while jj < len(grid[i])-1:
            jj += 1
            if grid[i][j] > grid[i][jj]:
                right += 1
            else:
                right += 1
                break

        # look down
        down = 0
        ii = i
        while ii < len(grid)-1:
            ii += 1
            if grid[i][j] > grid[ii][j]:
                down += 1
            else:
                down += 1
                break

        max_score = max(max_score, up * down * left * right)

print(max_score)