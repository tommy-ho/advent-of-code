import sys

# reading input
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

# part 1

def get_highest_happiness(orders):
    highest = sys.maxsize * -1
    for order in orders:
        rating = 0
        for i in range(0, len(order)-1):
            rating += happiness[order[i]][order[i+1]] + happiness[order[i+1]][order[i]]
        rating += happiness[order[0]][order[-1]] + happiness[order[-1]][order[0]]
        if rating > highest:
            highest = rating
            best_order = order
    return highest, best_order


happiness = {}

#parse happiness
for line in lines:
    split = line.split(' ')
    a = split[0]
    b = split[-1].strip()[0:-1]

    rating = int(split[3])
    rating = rating if split[2] == 'gain' else rating * -1

    if a not in happiness:
        happiness[a] = {}

    happiness[a][b] = rating

# get all the orders
orders = []
for person in happiness:
    orders.append([person])

while True:
    new_orders = []
    for order in orders:
        for person in happiness:
            if person not in order:
                new_order = order + [person]
                new_orders.append(new_order)
    orders = new_orders
    if len(orders[0]) == len(happiness):
        break

# identify highest happiness out of all orders
highest, best_order = get_highest_happiness(orders)
print(highest)
print(best_order)
print()

# part 2

#add me to happiness dict
happiness['me'] = {}
for person in happiness:
    if person != 'me':
        happiness['me'][person] = 0
        happiness[person]['me'] = 0

# get all the orders with me
orders = []
for i in range(len(best_order)+1):
    new_order = best_order.copy()
    new_order.insert(i, 'me')
    orders.append(new_order)

# identify highest happiness out of all orders
highest, best_order = get_highest_happiness(orders)
print(highest)
print(best_order)