import sys

N = int(sys.stdin.readline())
aArr = list(map(int, sys.stdin.readline().split()))

aArr.sort(reverse=True)
accArr = [0]
acc = 0
for entry in aArr:
    acc += entry
    accArr.append(acc)

largestTeamCount = 0
before = 0
for i in range(1, len(accArr)):
    if accArr[i] * i + (accArr[len(accArr)-1]-accArr[i]) >= before:
        largestTeamCount = i
        before = accArr[i] * i + (accArr[len(accArr)-1]-accArr[i])
answer = accArr[largestTeamCount] * largestTeamCount + (accArr[len(accArr)-1]-accArr[largestTeamCount])
print(answer)
