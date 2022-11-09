from hashlib import md5

input = 'iwrupvqb'
number = 0
result = None

# part 1

while True:
    test_input = (input + str(number)).encode()
    result = md5(test_input).hexdigest()
    if result[0:5] == '00000':
        break
    number += 1

print(number)

# part 2

number2 = 0

while True:
    test_input = (input + str(number2)).encode()
    result = md5(test_input).hexdigest()
    if result[0:6] == '000000':
        break
    number2 += 1

print(number2)