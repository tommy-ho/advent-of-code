# reading input
f = open('input.txt', 'r')
input = f.readlines()
instructions = [i.strip() for i in input]
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

    print(f'cycle {i+1} : {X * (i+1)}')

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