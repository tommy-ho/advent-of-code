import sys

# reading input
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

# part 1

# getting input into a dict

ingredients = {}

for line in lines:
    split = line.split(': ')
    name = split[0]
    split = split[1].split(', ')
    ingredients[name] = {}
    for property in split:
        property = property.split(' ')
        ingredients[name][property[0]] = int(property[1])
    
print(ingredients)

# identifying all permutations

teaspoons = 100
permutations = []

for i in range(teaspoons+1): # Sprinkles
    for j in range(teaspoons-i+1): # Butterscotch
        for k in range(teaspoons-i-j+1): #Chocolate
            candy = teaspoons - i - j - k
            permutations.append({
                'Sprinkles': i,
                'Butterscotch': j,
                'Chocolate': k,
                'Candy': candy
            })


# calculate the total score of all cookies and identifying the top

def get_top_score(permutations):
    top_score = -1 * sys.maxsize

    for permutation in permutations:
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0

        for item in permutation:
            capacity += permutation[item] * ingredients[item]['capacity']
            durability += permutation[item] * ingredients[item]['durability']
            flavor += permutation[item] * ingredients[item]['flavor']
            texture += permutation[item] * ingredients[item]['texture']
        
        capacity = max(capacity, 0)
        durability = max(durability, 0)
        flavor = max(flavor, 0)
        texture = max(texture, 0)

        top_score = max(top_score, capacity * durability * flavor * texture)

    return top_score

print(get_top_score(permutations))

# part 2
permutations = []

# new permutations given the calories constraint
for i in range(teaspoons+1): # Sprinkles
    for j in range(teaspoons-i+1): # Butterscotch
        for k in range(teaspoons-i-j+1): #Chocolate
            candy = teaspoons - i - j - k

            if i * ingredients['Sprinkles']['calories'] + \
            j * ingredients['Butterscotch']['calories'] + \
            k * ingredients['Chocolate']['calories'] + \
            candy * ingredients['Candy']['calories'] == 500:
                permutations.append({
                    'Sprinkles': i,
                    'Butterscotch': j,
                    'Chocolate': k,
                    'Candy': candy
                })

print(get_top_score(permutations))