import sys

# reading input
f = open('input.txt', 'r')
flights = f.readlines()
f.close()

# part 1

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