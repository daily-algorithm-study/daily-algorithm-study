import sys

C, N = map(int, sys.stdin.readline().split())
costToCustomer = {}
for i in range(N):
    cost, customer = map(int, sys.stdin.readline().split())
    if cost in costToCustomer and costToCustomer[cost] < customer:
        costToCustomer[cost] = customer
    elif cost not in costToCustomer:
        costToCustomer[cost] = customer

dp = [0 for _ in range(101000)]
for i in range(1, 101000):
    for cost in costToCustomer:
        if cost <= i:
            dp[i] = max(dp[i-1], dp[i], dp[i-cost]+costToCustomer[cost])
        else:
            dp[i] = max(dp[i], dp[i-1])

for i, customer in enumerate(dp):
    if i == 0:
        continue
    if customer >= C:
        print(i)
        break

