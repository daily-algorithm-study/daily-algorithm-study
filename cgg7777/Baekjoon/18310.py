import sys
# N = 2 * 10^5
# dist = 1 * 10^5

N = int(sys.stdin.readline())
homes = list(map(int, sys.stdin.readline().split()))
homes.sort()
dp = [0] * N

for index in range(1, len(homes)):
    dp[0] = dp[0] + abs(homes[index] - homes[0])

for index in range(1, len(homes)):
    dp[index] = dp[index-1] + (index-(len(homes)-index)) * (homes[index] - homes[index-1])

print(homes[dp.index(min(dp))])