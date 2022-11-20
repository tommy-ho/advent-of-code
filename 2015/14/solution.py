import sys

# reading input
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

# part 1

def parse_input(lines):
    dict = {} # Reindeer name as key : {speed, stamina, rest, current_stamina, current_rest, distance}
    for line in lines:
        split = line.split(' ')
        dict[split[0]] = {
            'speed' : int(split[3]), 
            'stamina' : int(split[6]), 
            'rest' : int(split[-2]), 
            'current_stamina' : int(split[6]), 
            'current_rest' : int(split[-2]),
            'distance' : 0,
            'points' : 0
        }
    return dict


def get_max_points(dict, score_system='distance'):
    max_points = sys.maxsize * -1
    for deer in dict:
        deer = dict[deer]
        max_points = max(deer[score_system], max_points)
    
    return max_points


dict = parse_input(lines)
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


print(get_max_points(dict))

# part 2

dict = parse_input(lines)
leaders = [] # deer name

for mile in range(1, race_end+1):
    for deer in dict:
        name = deer
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

        if len(leaders) == 0 or deer['distance'] > dict[leaders[0]]['distance']:
            leaders = [name]
        elif deer['distance'] == dict[leaders[0]]['distance'] and name not in leaders:
            leaders.append(name)

    for deer in leaders:
        dict[deer]['points'] += 1


print(get_max_points(dict, 'points'))
