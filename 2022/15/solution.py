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
sensors = {}

for line in lines:
    split = line.split('=')
    sx = int(split[1].split(',')[0])
    sy = int(split[2].split(':')[0])
    bx = int(split[3].split(',')[0])
    by = int(split[4].strip())

    dist = abs(sx-bx) + abs(sy-by)
    sensors[sx,sy] = dist



def reachable(coord):
    for s in sensors:
        # if any sensor can reach this coord, return True
        if sensors[s] >= abs(s[0] - coord[0]) + abs(s[1] - coord[1]):
            return True
    return False

pos = None

# iterate over every sensor's borders
for s in sensors:
    dist = sensors[s]

    for i in range(dist):
        # left borders
        left_up = (s[0] - dist + i - 1, s[1] + i)
        left_down = (s[0] - dist + i - 1, s[1] - i)
        # right borders
        right_up = (s[0] + dist - i + 1, s[1] + i)
        right_down = (s[0] + dist - i + 1, s[1] - i)

        for border in [left_up, left_down, right_up, right_down]:
            if 0 <= border[0] <= max and 0 <= border[1] <= max and not reachable(border):
                pos = border
                break
        
        if pos is not None:
            break
    
    if pos is not None:
        break


ans = pos[0] * 4000000 + pos[1]
print(ans)