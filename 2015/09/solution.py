import sys

# reading input
f = open('input.txt', 'r')
flights = f.readlines()
f.close()

# part 1 - this approach does not always work if there are shortest/longest path 
# that does not immediately take the most optimal option

cost_table = {}
cities = set()

for flight in flights:
    split = flight.split(' = ')
    cost = split[1]
    locations = split[0].split(' to ')
    source = locations[0]
    destination = locations[1]
    dist = int(cost.strip())
    cost_table[(source,destination)] = dist
    cost_table[(destination,source)] = dist
    cities.add(source)
    cities.add(destination)

# init ans matrix and remaining_flights list for all start cities
matrix = {}
remaining_flights = {}
for city in cities:
    matrix[city] = 0
    remaining_flights[city] = [x for x in list(cost_table) if city not in x[1]]


for start in cities:
    current = start
    traveled = 1
    while (traveled < len(cities)):
        lowest_cost = sys.maxsize
        dest = None

        # select shortest flight
        for flight in remaining_flights[start]:
            if current in flight[0] and cost_table[flight] < lowest_cost:
                lowest_cost = cost_table[flight]
                dest = flight[1]
        
        # update current location
        current = dest
        matrix[start] += lowest_cost
        traveled += 1

        # remove all flights that has current location as a destination
        for flight in remaining_flights[start]:
            if current in flight[1]:
                remaining_flights[start].remove(flight)
        

shortest = min(matrix.items(), key=lambda x: x[1])
print(shortest)



# slightly less ideal path might lead to a better outcome, see below
# dist = 804
# Faerun selected longest flight to Norrath with dist 129
# Norrath selected longest flight to Tristram with dist 142
# Tristram selected longest flight to AlphaCentauri with dist 118       
# AlphaCentauri selected longest flight to Arbre with dist 116
# Arbre selected longest flight to Snowdin with dist 129
# Snowdin selected longest flight to Straylight with dist 99
# Straylight selected longest flight to Tambi with dist 70

# dist < 804
# Faerun selected longest flight to Norrath with dist 129
# Norrath selected longest flight to Tristram with dist 142
# Tristram selected longest flight to Arbre with dist 122
# Arbre selected longest flight to Snowdin with dist 129
# Snowdin selected longest flight to Straylight with dist 99
# Straylight selected longest flight to AlphaCentauri with dist 91      
# AlphaCentauri selected longest flight to Tambi with dist 18


# part 2 - this approach solves both parts

# capture all possible path permutations and then calculate them using cost table

paths = []
for city in cities:
    paths.append([city])

while True:
    new_paths = []
    for path in paths:
        for city in cities:
            if city not in path:
                new_path = path + [city]
                new_paths.append(new_path)
    paths = new_paths
    if len(paths[0]) == len(cities):
        break

highest = 0
lowest = sys.maxsize

for path in paths:
    dist = 0
    for i in range(0, len(path)-1):
        dist += cost_table[(path[i], path[i+1])]
    highest = max(dist, highest)
    lowest = min(dist, lowest)

print(lowest)
print(highest)