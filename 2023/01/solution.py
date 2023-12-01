# reading input
f = open('input.txt', 'r')
input = f.readlines()
lines = [i.strip() for i in input]
f.close()

# part 1

ans = 0

for line in lines:
    first = None
    last = None
    for c in line:
        if c.isnumeric():
            if first == None:
                first = c
            last = c
    ans += int(first + last)

print(ans)


# part 2

ans = 0

for line in lines:
    first = None
    last = None
    for i in range(len(line)):
        c = line[i]
        if c.isnumeric():
            if first == None:
                first = c
            last = c
        else:
            converted = None
            if line[i:].startswith("one"):
                converted = "1"
            elif line[i:].startswith("two"):
                converted = "2"
            elif line[i:].startswith("three"):
                converted = "3"
            elif line[i:].startswith("four"):
                converted = "4"
            elif line[i:].startswith("five"):
                converted = "5"
            elif line[i:].startswith("six"):
                converted = "6"
            elif line[i:].startswith("seven"):
                converted = "7"
            elif line[i:].startswith("eight"):
                converted = "8"
            elif line[i:].startswith("nine"):
                converted = "9"

            if converted != None:
                if first == None:
                    first = converted
                last = converted
    ans += int(first + last)

print(ans)