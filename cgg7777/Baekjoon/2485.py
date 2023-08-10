import sys

N = int(sys.stdin.readline())
trees = []
for i in range(N):
    trees.append(int(sys.stdin.readline()))

def gcd(a, b):
    if a < b:
        a, b = b, a
    while(True):
        c = a % b
        if c == 0:
            return b
        a = b
        b = c
distances = [trees[i] - trees[i+1] for i in range(len(trees)-1)]

answer = 0
gcdValue = gcd(distances[0] , distances[1])
for i in range(2, len(distances)):
    gcdValue = gcd(gcdValue, distances[i])

for entry in distances:
    answer += entry // gcdValue - 1

print(answer)

