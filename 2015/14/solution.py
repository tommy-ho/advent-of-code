import sys

# reading input
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

dict = {} # Reindeer name as key : (speed, stamina, rest, current_stamina, current_rest)
for line in lines:
    split = line.split(' ')
    dict[split[0]] = {
        'speed' : int(split[3]), 
        'stamina' : int(split[6]), 
        'rest' : int(split[-2]), 
        'current_stamina' : int(split[6]), 
        'current_rest' : int(split[-2]),
        'distance' : 0
    }

print(dict)

race_end = 2503


for mile in range(1, race_end+1):
    for deer in dict:
        deer = dict[deer]
        if deer['current_stamina'] > 0:
            deer['distance'] += deer['speed']
            deer['current_stamina'] -= 1
        elif deer['current_rest'] > 0:
            deer['current_rest'] -= 1
        else: # finished resting
            deer['current_stamina'] = deer['stamina']
            deer['current_rest'] = deer['rest']
            deer['distance'] += deer['speed']
            deer['current_stamina'] -= 1

print(dict)

max_dist = sys.maxsize * -1

for deer in dict:
    deer = dict[deer]
    max_dist = max(deer['distance'], max_dist)

print(max_dist)
