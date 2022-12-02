# reading input
f = open('input.txt', 'r')
lines = f.readlines()
lines = [i.strip() for i in lines]
f.close()

# part 1
total = 0

for line in lines:
    split = line.split(' ')
    opp = split[0]
    me = split[1]

    if opp == 'A': # opponent is rock
        if me == 'X':
            total += 4 # 1 pt for picking rock, 3 pt for tie
        elif me == 'Y':
            total += 8 # 2 pt for picking scissor, 6 pt for winning
        else:
            total += 3 # 3 pt for picking scissor, 0 pt for losing
    elif opp == 'B': # opponent is paper
        if me == 'X':
            total += 1 # 1 pt for picking rock, 0 pt for losing
        elif me == 'Y':
            total += 5 # 2 pt for picking scissor, 3 pt for tie
        else:
            total += 9 # 3 pt for picking scissor, 6 pt for winning
    else: # opponent is scissor
        if me == 'X':
            total += 7 # 1 pt for picking rock, 6 pt for winning
        elif me == 'Y':
            total += 2 # 2 pt for picking scissor, 0 pt for losing
        else:
            total += 6 # 3 pt for picking scissor, 3 pt for tie

print(total)


# part 2
total = 0

for line in lines:
    split = line.split(' ')
    opp = split[0]
    me = split[1]

    if opp == 'A': # opponent is rock
        if me == 'X': # need to lose
            total += 3 # 3 pt for picking scissor, 0 pt for losing
        elif me == 'Y': # need to draw
            total += 4 # 1 pt for picking rock, 3 pt for tie
        else: # need to win
            total += 8 # 2 pt for picking paper, 6 pt for winning
    elif opp == 'B': # opponent is paper
        if me == 'X': # need to lose
            total += 1 # 1 pt for picking rock, 0 pt for losing
        elif me == 'Y': # need to draw
            total += 5 # 2 pt for picking paper, 3 pt for tie
        else: # need to win
            total += 9 # 3 pt for picking scissor, 6 pt for winning
    else: # opponent is scissor
        if me == 'X': # need to lose
            total += 2 # 2 pt for picking paper, 0 pt for losing
        elif me == 'Y': # need to draw
            total += 6 # 3 pt for picking scissor, 3 pt for tie
        else: # need to win
            total += 7 # 1 pt for picking rock, 6 pt for winning

print(total)