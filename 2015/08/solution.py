import re

# reading input
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

# part 1

ans = 0

for line in lines:
    line = line.strip()
    total = len(line)
    chars_in_memory = 0

    if len(line) > 2:
        matches = re.findall(r'\\\"', line)
        chars_in_memory += len(matches)
        line = re.sub(r'\\\"', '', line)

        matches = re.findall(r'\\\\', line)
        chars_in_memory += len(matches)
        line = re.sub(r'\\\\', '', line)

        matches = re.findall(r'\\x[0-9a-f]{2}', line)
        chars_in_memory += len(matches)
        line = re.sub(r'\\x[0-9a-f]{2}', '', line)

    chars_in_memory += len(line) #remaining chars
    chars_in_memory -= 2    #2 for the leading and trailing quotes

    ans += total - chars_in_memory

print(ans)


# part 2

ans = 0

for line in lines:
    line = line.strip()
    total = len(line)
    encoded_total = 0

    matches = re.findall(r'\"', line)
    encoded_total += len(matches) * 2
    line = re.sub(r'\"', '', line)

    matches = re.findall(r'\\', line)
    encoded_total += len(matches) * 2
    line = re.sub(r'\\', '', line)

    encoded_total += len(line) + 2 #remaining chars and surrounding quotes

    ans += encoded_total - total

print(ans)