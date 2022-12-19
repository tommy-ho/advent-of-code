from math import gcd

# reading input
f = open('input.txt', 'r')
input = f.readlines()
lines = [i.strip() for i in input]
f.close()

class Monkey():
    def __init__(self, lines):
        self.id = lines[0].split(' ')[1][0:-1]
        item_str = lines[1].split(': ')[1].split(', ')
        self.items = [int(i) for i in item_str]
        self.op = lines[2].split(': ')[1]
        self.div_test = int(lines[3].split(' ')[-1])
        self.if_true = lines[4].split(' ')[-1]
        self.if_false = lines[5].split(' ')[-1]
        self.inspected = 0


# part 1

# construct list of monkeys
monkeys = {}
for i in range(len(lines)):
    if lines[i].startswith('Monkey'):
        m = Monkey(lines[i:i+6])
        monkeys[m.id] = m

for r in range(20):
    for m in monkeys:
        m = monkeys[m]
        print(f'Monkey {m.id}:')
        while len(m.items) > 0:
            old = m.items.pop(0) #old worry level
            print(f' Monkey inspects an item with a worry level of {old}.')
            new = None
            exec(m.op)
            print(f'  New worry level is {new}')
            worry = new // 3
            print(f'  Divided by 3 to get {worry}')

            if worry % m.div_test == 0:
                print(f'  Item with worry level {worry} is thrown to monkey {m.if_true}')
                monkeys[m.if_true].items.append(worry)
            else:
                print(f'  Item with worry level {worry} is thrown to monkey {m.if_false}')
                monkeys[m.if_false].items.append(worry)

            m.inspected += 1
    
    print(f'\nRound {r+1} summary:')
    for m in monkeys:
        m = monkeys[m]
        print(m.id)
        print(m.items)
        print(m.inspected)
        print()

inspections = sorted([m.inspected for m in monkeys.values()])
print(inspections[-1] * inspections[-2])


# part 2

# construct list of monkeys
monkeys = {}
for i in range(len(lines)):
    if lines[i].startswith('Monkey'):
        m = Monkey(lines[i:i+6])
        monkeys[m.id] = m

# get LCM of all monkey div tests to be used to reduce worry level
div_tests = [m.div_test for m in monkeys.values()]
lcm = 1
for i in div_tests:
    lcm = lcm * i // gcd(lcm, i)


for r in range(10000):
    for m in monkeys:
        m = monkeys[m]
        while len(m.items) > 0:
            old = m.items.pop(0) #old worry level
            new = None
            exec(m.op)
            worry = new % lcm

            if worry % m.div_test == 0:
                monkeys[m.if_true].items.append(worry)
            else:
                monkeys[m.if_false].items.append(worry)

            m.inspected += 1
    

inspections = sorted([m.inspected for m in monkeys.values()])
print(inspections[-1] * inspections[-2])