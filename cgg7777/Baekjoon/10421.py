import sys
from itertools import product

N = int(sys.stdin.readline())
SArr = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
KArr = list(map(int, sys.stdin.readline().split()))
setKArr = set(map(str, KArr))

answer = 0
def recursiveTest(s1: str, s2: list[int], depth: int, s : list[int]):
    global answer
    if len(s2) == depth:
        lastSum = str(s[0] + s[1] * 10 + s[2] * 100)
        if len(str(lastSum)) != SArr[-1] or set(str(lastSum)) - setKArr:
            return False
        else:
            answer +=1
            return True

    for num in KArr:
        s2[depth] = num
        row = str(s2[depth] * int(s1))
        if len(row) == SArr[depth+2] and not(set(row) - setKArr):
            s[depth] = int(row)
            recursiveTest(s1, s2, depth + 1, s)


s1Arr = product(KArr, repeat=SArr[0])
for s1 in s1Arr:
    s2 = [0] * SArr[1]
    recursiveTest(''.join(map(str, s1)), s2, 0, [0, 0, 0])

print(answer)
