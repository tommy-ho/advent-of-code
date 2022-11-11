# same code works for pt 1 and pt 2 (albeit a bit slower)

def look_and_say(input, iterations):
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
        
        # add to temp the last sequence if any
        temp += str(count) + val

        iterations -= 1
        input = temp

    return len(input)

# part 1
input = '1321131112'
print(look_and_say(input, 40))

# part 2
print(look_and_say(input, 50))