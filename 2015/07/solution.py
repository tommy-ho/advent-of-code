# reading input
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

# part 1

instructions = {}
signals = {}

for x in lines:
    x_split = x.split(' -> ')
    var = x_split[-1].strip()
    instructions[var] = x_split[0].split(' ')

def identify(x):
    if x.isnumeric():
        return int(x)
    
    if x in signals:
        return signals[x]

    # recursively solve for x because is has not be identified yet
    instr = instructions[x]

    if len(instr) == 1:
        res = identify(instr[0])
    elif instr[0] == 'NOT':
        res = ~ identify(instr[1]) & 65535
    else:
        first = instr[0]
        second = instr[2]
        ops = instr[1]
        if ops == 'AND':
            res = identify(first) & identify(second)
        elif ops == 'OR':
            res = identify(first) | identify(second)
        elif ops == 'LSHIFT':
            res = identify(first) << identify(second) & 65535
        else:
            res = identify(first) >> identify(second)

    signals[x] = res
    return res

a = identify('a')
print(a)

# part 2

instructions['b'] = [str(a)]
signals = {}

a = identify('a')
print(a)
