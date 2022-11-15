import json

# reading input
f = open('input.txt', 'r')
data = json.load(f)
f.close()

# part 1

# def search(data):
#     if type(data) is int:
#         return data
#     elif type(data) is str:
#         return 0
    
#     sum = 0
#     for key in data:
#         if type(key) is int:
#             sum += key
#         elif type(key) in [list, dict]:
#             sum += search(key)    
#         elif type(key) is str and type(data) is dict: # not list
#             sum += search(data[key])

#     return sum

# sum = search(data)
# print(sum)

# part 2

def search(data):
    if type(data) is dict and 'red' in data.values():
        return 0
    elif type(data) is int:
        return data
    elif type(data) is str:
        return 0
    
    sum = 0
    for key in data:
        if type(key) is int:
            sum += key
        elif type(key) in [list, dict]:
            sum += search(key)    
        elif type(key) is str and type(data) is dict: # not list
            sum += search(data[key])

    return sum

sum = search(data)
print(sum)