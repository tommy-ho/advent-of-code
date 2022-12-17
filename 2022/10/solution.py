# reading input
f = open('input.txt', 'r')
input = f.readlines()
instructions = [i.strip() for i in input]
instructions2 = instructions.copy()
f.close()

# part 1

def is_cycle(i):
    if (i - 20) % 40 == 0:
        return True
    return False

cycles = 220
signal_strengths = []
X = 1 # register starts at 1
wait = False
to_add = None

for i in range(0, cycles):
    if is_cycle(i+1):
        signal_strengths.append(X * (i+1))

    # print(f'cycle {i+1} : {X * (i+1)}')

    if wait:
        X += to_add
        wait = False
    else:
        # cycle through the instructions
        instr = instructions.pop(0)
        instructions.append(instr)

        if instr != 'noop':
            split = instr.split(' ')
            to_add = int(split[1])
            wait = True
    

print(sum(signal_strengths))

# part 2

cycles = 240
pixels = []
X = 1 # register starts at 1
wait = False
to_add = None

for i in range(0, cycles):
    position = i % 40
    if position in [X-1, X, X+1]:
        pixels.append('#')
    else:
        pixels.append('.')

    # print(f'cycle {i+1} : {X}')

    if wait:
        X += to_add
        wait = False
    else:
        # cycle through the instructions
        instr = instructions2.pop(0)
        instructions2.append(instr)

        if instr != 'noop':
            split = instr.split(' ')
            to_add = int(split[1])
            wait = True
    

row_limit = 40
current_row = ''
for i in range(len(pixels)):
    if row_limit > 0:
        current_row += pixels[i]
        row_limit -= 1
    if row_limit == 0:
        print(current_row)
        current_row = ''
        row_limit = 40