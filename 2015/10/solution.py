input = '1321131112'
iterations = 40

while (iterations > 0):
    temp = ''
    val = None
    count = 0

    for i in range(len(input)):
        if val is None: # start
            val = input[i]
            count += 1
        elif input[i] == val: # same letter as before
            count += 1
        else: # diff letter, append to temp the last sequence
            temp += str(count) + val
            val = input[i]
            count = 1
    
    temp += str(count) + val
    # print(f'count is {count}')
    # print(f'val is {val}')
    # print(temp)

    iterations -= 1
    input = temp

print(len(input))