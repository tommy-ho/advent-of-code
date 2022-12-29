# reading input
f = open('input.txt', 'r')
input = f.readlines()
lines = [i.strip() for i in input]
f.close()

# part 1 - construct grid where no sensors can be

grid = {}
row = 2000000
beacons = []

for line in lines:
    split = line.split('=')
    sx = int(split[1].split(',')[0])
    sy = int(split[2].split(':')[0])
    bx = int(split[3].split(',')[0])
    by = int(split[4].strip())

    beacons.append((bx,by)) # add a list of beacons to remove from list later

    dist = abs(sx-bx) + abs(sy-by)

    if dist < abs(sy-row): # skip if row is too far from sensor
        continue

    dist -= abs(sy-row) # decrease dist by distance from row

    for i in range(sx - dist, sx + dist + 1):
        grid[i, row] = '#'

# remove beacons from list of not possible
for beacon in beacons:
    if beacon in grid:
        del grid[beacon]

print(len(grid))


# part 2

max = 4000000
grid = {}
beacons = []

x_counter = 0
y_counter = 0

for line in lines:
    split = line.split('=')
    sx = int(split[1].split(',')[0])
    sy = int(split[2].split(':')[0])
    bx = int(split[3].split(',')[0])
    by = int(split[4].strip())

    beacons.append((bx,by)) # add a list of beacons to remove from list later

    dist = abs(sx-bx) + abs(sy-by)

    for row in range(max):            
        if dist < abs(sy-row): # skip if row is too far from sensor
            continue

        start = sx - (dist - abs(sy-row))
        end = sx + (dist - abs(sy-row))
        for i in range(start, end + 1):
            grid[i, row] = '#'


for x in range(max):
    for y in range(max):
        if (x,y) not in grid:
            print(f'{x}  {y}')
            print(x*4000000 + y)