import sys

adjMatrix = [[False for _ in range(60)] for i in range(60)]

N = int(sys.stdin.readline())
dic = {}
for i in range(N):
    start, _, end = sys.stdin.readline().split()
    if start == end:
        continue
    if start not in dic:
        dic[start] = set(end)
    else:
        dic[start].add(end)

keys = [key for key in dic]
keys.sort()
for key in keys:
    for entry in dic[key]:
        adjMatrix[ord(key)-65][ord(entry)-65] = True

for k in range(60):
    for i in range(60):
        for j in range(60):
            if i != j and adjMatrix[i][k] and adjMatrix[k][j]:
                adjMatrix[i][j] = True

answer = {}
total = 0
for key in keys:
    index = ord(key)-65
    for i in range(60):
        if adjMatrix[index][i]:
            total += 1
            if key not in answer:
                answer[key] = [chr(i+65)]
            else:
                answer[key].append(chr(i+65))
print(total)
for key in keys:
    for entry in answer[key]:
        print(str(key) + " => " + str(entry))
