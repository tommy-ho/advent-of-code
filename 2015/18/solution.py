# reading input
f = open('input.txt', 'r')
lines = f.readlines()
lines = [i.strip() for i in lines]
f.close()

# part 1

# define a table for the lights
lights = []
for i in range(len(lines)):
    lights.append([])
    for j in range(len(lines[i])):
        lights[i].append(lines[i][j])


# function for debugging
def print_lights(lights):
    for line in lights:
        l = ''
        for c in line:
            l += c
        print(l)
    print()


print_lights(lights)

directions = [(-1,-1), (-1,0), (-1,1), (1,1), (1,0), (1,-1), (0,1), (0,-1)]
rounds = 100

for i in range(rounds):
    current_lights = [x[:] for x in lights]
    total_lights_on = 0
    for x in range(len(lights)):
        for y in range(len(lights[x])):
            neighbors_on = 0
            for d in directions:
                xd = x+d[0]
                yd = y+d[1]
                if xd < 0 or yd < 0 or xd >= len(lights) or yd >= len(lights[x]):
                    continue
                if current_lights[xd][yd] == '#':
                    neighbors_on += 1
            if current_lights[x][y] == '#' and neighbors_on in [2,3]:
                total_lights_on += 1
            else:
                lights[x][y] = '.'
            
            if current_lights[x][y] == '.' and neighbors_on == 3:
                total_lights_on += 1
                lights[x][y] = '#'

                
print(total_lights_on)


# part 2

# define a table for the lights
lights = []
for i in range(len(lines)):
    lights.append([])
    for j in range(len(lines[i])):
        lights[i].append(lines[i][j])

# turn the 4 corners on
end = len(lights)-1
lights[0][0] = '#'
lights[0][end] = '#'
lights[end][0] = '#'
lights[end][end] = '#'

for i in range(rounds):
    current_lights = [x[:] for x in lights]
    total_lights_on = 4 #default to 4 because the 4 corners stay on
    for x in range(len(lights)):
        for y in range(len(lights[x])):
            if (x,y) in [(0,0),(0,end),(end,0),(end,end)]:
                continue
            neighbors_on = 0
            for d in directions:
                xd = x+d[0]
                yd = y+d[1]
                if xd < 0 or yd < 0 or xd >= len(lights) or yd >= len(lights[x]):
                    continue
                if current_lights[xd][yd] == '#':
                    neighbors_on += 1
            if current_lights[x][y] == '#' and neighbors_on in [2,3]:
                total_lights_on += 1
            else:
                lights[x][y] = '.'
            
            if current_lights[x][y] == '.' and neighbors_on == 3:
                total_lights_on += 1
                lights[x][y] = '#'

                
print(total_lights_on)