# reading input
f = open('input.txt', 'r')
input = f.readlines()
lines = [i.strip() for i in input]
f.close()

# part 1

ans = 0

for line in lines:
    winning, selected = line.split(" | ")
    game, winning = winning.split(": ")
    winning = winning.replace("  ", " ").strip()
    winning = winning.split(" ")

    selected = selected.replace("  ", " ").strip()
    selected = selected.split(" ")

    match_count = 0
    for selection in selected:
        if selection in winning:
            match_count += 1

    if match_count > 0:
        ans += 2**(match_count-1)

print(ans)


# part 2

count = 0
multiplier = {}

for line in lines:
    winning, selected = line.split(" | ")
    game, winning = winning.split(": ")
    game = int(game.split(" ")[-1].strip())
    winning = winning.replace("  ", " ").strip()
    winning = winning.split(" ")

    selected = selected.replace("  ", " ").strip()
    selected = selected.split(" ")

    times_to_run = multiplier[game] + 1 if game in multiplier else 1
    count += times_to_run

    match_count = 0
    for selection in selected:
        if selection in winning:
            match_count += 1

    while match_count > 0:
        if game + match_count not in multiplier:
            multiplier[game + match_count] = 0    
        multiplier[game + match_count] += times_to_run
        match_count -= 1
        


print(count)