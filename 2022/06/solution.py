# reading input
f = open('input.txt', 'r')
input = f.read().strip()
f.close()

# part 1

for i in range(3, len(input)):
    unique = set()
    unique.add(input[i-3])
    unique.add(input[i-2])
    unique.add(input[i-1])
    unique.add(input[i])
    if len(unique) == 4:
        print(i+1)
        break

# part 2

for i in range(13, len(input)):
    unique = set()
    for j in range(14):
        unique.add(input[i-j])
    if len(unique) == 14:
        print(i+1)
        break