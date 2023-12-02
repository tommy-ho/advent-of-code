# reading input
f = open('input.txt', 'r')
input = f.readlines()
lines = [i.strip() for i in input]
f.close()

# part 1

limit = {
    "red": 12,
    "green": 13,
    "blue": 14
}

ans = 0

for line in lines:
    game, sets = line.split(": ")
    id = int(game.split(" ")[1])
    sets = sets.split("; ")
    is_valid = True

    for set in sets:
        counts = set.split(", ")
        for count in counts:
            num, color = count.split(" ")
            num = int(num)
            if num > limit[color]:
                is_valid = False
                break
        if is_valid == False:
            break
        
    if is_valid == True:
        ans += id

print(ans)
