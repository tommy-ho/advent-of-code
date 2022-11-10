import re

# reading input
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

# part 1

ans = 0

for line in lines:
    line = line.strip()
    print(line)
    total = len(line)
    chars_in_memory = 0

    if len(line) > 2:
        matches = re.findall(r'\\\"', line)
        chars_in_memory += len(matches)
        line = re.sub(r'\\\"', '', line)
        print(f'chars in mem {chars_in_memory}')

        matches = re.findall(r'\\\\', line)
        chars_in_memory += len(matches)
        line = re.sub(r'\\\\', '', line)
        print(f'chars in mem {chars_in_memory}')

        matches = re.findall(r'\\x[0-9a-f]{2}', line)
        chars_in_memory += len(matches)
        line = re.sub(r'\\x[0-9a-f]{2}', '', line)
        print(f'chars in mem {chars_in_memory}')

    print(line)
    chars_in_memory += len(line) #remaining chars
    chars_in_memory -= 2    #2 for the leading and trailing quotes
    print(f'total {total}')
    print(f'chars in mem {chars_in_memory}')

    ans += total - chars_in_memory
    print(ans)
    print()