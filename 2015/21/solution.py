from copy import deepcopy
from sys import maxsize

# reading input
f = open('input.txt', 'r')
lines = f.readlines()
lines = [i.strip() for i in lines]
f.close()

# part 1

boss = {}

for line in lines:
    split = line.split(': ')
    boss[split[0]] = int(split[1].strip())

weapons = {}
armors = {}
rings = {}

weapons['Dagger'] = {'Cost': 8, 'Damage': 4, 'Armor': 0}
weapons['Shortsword'] = {'Cost': 10, 'Damage': 5, 'Armor': 0}
weapons['Warhammer'] = {'Cost': 25, 'Damage': 6, 'Armor': 0}
weapons['Longsword'] = {'Cost': 40, 'Damage': 7, 'Armor': 0}
weapons['Greataxe'] = {'Cost': 74, 'Damage': 8, 'Armor': 0}

armors['None'] = {'Cost': 0, 'Damage': 0, 'Armor': 0}
armors['Leather'] = {'Cost': 13, 'Damage': 0, 'Armor': 1}
armors['Chainmail'] = {'Cost': 31, 'Damage': 0, 'Armor': 2}
armors['Splintmail'] = {'Cost': 53, 'Damage': 0, 'Armor': 3}
armors['Bandedmail'] = {'Cost': 75, 'Damage': 0, 'Armor': 4}
armors['Platemail'] = {'Cost': 102, 'Damage': 0, 'Armor': 5}

rings['None'] = {'Cost': 0, 'Damage': 0, 'Armor': 0}
rings['Damage +1'] = {'Cost': 25, 'Damage': 1, 'Armor': 0}
rings['Damage +2'] = {'Cost': 50, 'Damage': 2, 'Armor': 0}
rings['Damage +3'] = {'Cost': 100, 'Damage': 3, 'Armor': 0}
rings['Defense + 1'] = {'Cost': 20, 'Damage': 0, 'Armor': 1}
rings['Defense + 2'] = {'Cost': 40, 'Damage': 0, 'Armor': 2}
rings['Defense + 3'] = {'Cost': 80, 'Damage': 0, 'Armor': 3}

# returns true if player wins
def battle(player, boss):
    players_turn = True
    while player['Hit Points'] > 0 and boss['Hit Points'] > 0:
        if players_turn:
            dmg = player['Damage'] - boss['Armor']
            dmg = dmg if dmg > 0 else 1
            boss['Hit Points'] -= dmg
            players_turn = False
        else:
            dmg = boss['Damage'] - player['Armor']
            dmg = dmg if dmg > 0 else 1
            player['Hit Points'] -= dmg
            players_turn = True    
    
    return boss['Hit Points'] <= 0

# identify all combinations of equipment and run simulations

loadouts = []

# loadouts are duplicated (rings1, ring2) vs (ring2, ring1), but otherwise works
for w in weapons:
    w_name = w
    w = weapons[w]
    player = {'Hit Points': 100, 'Damage': 0, 'Armor': 0, 'Spent': 0}
    player['Damage'] = w['Damage']
    player['Spent'] += w['Cost']
    for a in armors:
        p = deepcopy(player)
        a_name = a
        a = armors[a]
        p['Armor'] = a['Armor']
        p['Spent'] += a['Cost']
        for r1 in rings:
            i = deepcopy(p)
            r1_name = r1
            r1 = rings[r1]
            i['Damage'] += r1['Damage']
            i['Armor'] += r1['Armor']
            i['Spent'] += r1['Cost']
            for r2 in rings:
                j = deepcopy(i)
                r2_name = r2
                r2 = rings[r2]
                if r2_name != 'None' and r2_name == r1_name:
                    continue
                j['Damage'] += r2['Damage']
                j['Armor'] += r2['Armor']
                j['Spent'] += r2['Cost']
                loadouts.append(j)

lowest_cost = maxsize

for p in deepcopy(loadouts):
    b = deepcopy(boss)
    if battle(p, b):
        lowest_cost = min(lowest_cost, p['Spent'])

print(lowest_cost)


# part 2

highest_cost = maxsize * -1

for p in deepcopy(loadouts):
    b = deepcopy(boss)
    if not battle(p, b):
        highest_cost = max(highest_cost, p['Spent'])

print(highest_cost)