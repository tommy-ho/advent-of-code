from itertools import combinations
import sys

# reading input
f = open('input.txt', 'r')
lines = f.readlines()
containers = [int(i) for i in lines]
f.close()

# part 1 - DP

containers.sort()
containers.insert(0, 0)
liters = 150

# define dp table and base cases
dp = []
for i in range(len(containers)):
    dp.append([])
    for j in range(liters+1):
        dp[i].append(0)


for i in range(1, len(containers)):
    for j in range(liters+1):
        container = containers[i]
        if container == j:
            dp[i][j] += 1
        elif container <= j and dp[i-1][j-container] > 0:
            dp[i][j] += dp[i-1][j-container]
        dp[i][j] += dp[i-1][j]


print(dp[-1][-1])


# part 2 - brute force all combinations

# combos = []
# for i in range(1, len(containers)):
#     for combo in combinations(containers, i):
#         combos.append(combo)

combos = [[]]
for i in containers:
    combos = combos + [combo + [i] for combo in combos]

min_containers_used = sys.maxsize
ans = 0

for combo in combos:
    if sum(combo) == liters:
        if len(combo) < min_containers_used:
            ans = 1
            min_containers_used = len(combo)
        elif len(combo) == min_containers_used:
            ans += 1

print(ans)