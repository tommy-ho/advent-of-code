from sys import maxsize
from copy import deepcopy

# reading input
f = open('input.txt', 'r')
input = f.readlines()
lines = [i.strip() for i in input]
f.close()

# set up grid

grid = []
dist = [] # (visited or not, shortest paths from S to each node)

start = None
end = None

for i in range(len(lines)):
    grid.append([])
    dist.append([])
    for j in range(len(lines[i])):
        d = maxsize
        ch = lines[i][j]
        if ch == 'S':
            start = (i,j)
            ch = 'a'
        elif ch == 'E':
            end = (i,j)
            ch = 'z'
        
        h = ord(ch) - 96
        grid[-1].append(h)
        dist[-1].append([False, d])


# part 1

def dijkstras(start, end, grid, dist):
    # set start to visited
    dist[start[0]][start[1]] = [True, 0]

    queue = []
    queue.append((start, 0))

    while len(queue) > 0:
        node = queue.pop(0)[0]
        i = node[0]
        j = node[1]
        dist[i][j][0] = True

        # check neighbors and update dist
        if 0 <= i-1 <= len(grid)-1 and 0 <= j <= len(grid[i])-1 and grid[i-1][j] <= grid[i][j]+1:
            dist[i-1][j][1] = min(dist[i-1][j][1], dist[i][j][1] + 1)
            neighbor = ((i-1,j), dist[i-1][j][1])
            if dist[i-1][j][0] is False and neighbor not in queue:
                queue.append(neighbor)


        if 0 <= i+1 <= len(grid)-1 and 0 <= j <= len(grid[i])-1 and grid[i+1][j] <= grid[i][j]+1:
            dist[i+1][j][1] = min(dist[i+1][j][1], dist[i][j][1] + 1)
            neighbor = ((i+1,j), dist[i+1][j][1])
            if dist[i+1][j][0] is False and neighbor not in queue:
                queue.append(neighbor)

        if 0 <= i <= len(grid)-1 and 0 <= j-1 <= len(grid[i])-1 and grid[i][j-1] <= grid[i][j]+1:
            dist[i][j-1][1] = min(dist[i][j-1][1], dist[i][j][1] + 1)
            neighbor = ((i,j-1), dist[i][j-1][1])
            if dist[i][j-1][0] is False and neighbor not in queue:
                queue.append(neighbor)

        if 0 <= i <= len(grid)-1 and 0 <= j+1 <= len(grid[i])-1 and grid[i][j+1] <= grid[i][j]+1:
            dist[i][j+1][1] = min(dist[i][j+1][1], dist[i][j][1] + 1)
            neighbor = ((i,j+1), dist[i][j+1][1])
            if dist[i][j+1][0] is False and neighbor not in queue:
                queue.append(neighbor)

        queue.sort(key = lambda x: x[1])

    return dist[end[0]][end[1]][1]

print(dijkstras(start, end, grid, deepcopy(dist)))


# part 2

possible_starts = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            possible_starts.append((i,j))

shortest_path = maxsize

for start in possible_starts:
    shortest_path = min(shortest_path, dijkstras(start, end, grid, deepcopy(dist)))

print(shortest_path)