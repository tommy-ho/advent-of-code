# reading input
f = open('input.txt', 'r')
lines = f.readlines()
containers = [int(i) for i in lines]
f.close()

# part 1

containers.sort()
containers.insert(0, 0)

liters = 150

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

i = 0
for row in dp:
    print(containers[i])
    print(row)
    print()
    i += 1