import sys
import math

# N <= 20, M <=20
N, M = map(int, sys.stdin.readline().split())

# 열쇠가 배치 되는 전체 경우의 수 = N!
total = math.factorial(N)

def divideNumber(leftValue, divideNum, start):
    answerList = []
    if divideNum !=1:
        for candidate in range(start, leftValue//divideNum +1):
            tempLists = divideNumber(leftValue - candidate, divideNum-1, candidate)
            for tempList in tempLists:
                answerList.append([candidate] + tempList)
    else:
        answerList.append([leftValue])
    return answerList


def countCase(N, bombNum):
    count = 0
    if bombNum == 1:
        return math.factorial(N-1)
    possibleCaseList = divideNumber(N, bombNum, 1)
    for case in possibleCaseList:
        leftValue = N
        tempCount = 1
        countDuplicate = {}
        for entry in case:
            tempCount *= math.factorial(entry-1)
            tempCount *= math.comb(leftValue, entry)
            leftValue -= entry
            if entry not in countDuplicate:
                countDuplicate[entry] = 1
            else:
                countDuplicate[entry] += 1
        for key in countDuplicate:
            tempCount //= math.factorial(countDuplicate[key])
        count += tempCount
    return count

def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a

answer = 0
for i in range(1, M+1):
    answer += countCase(N, i)

gcdValue = gcd(total, answer)
total //= gcdValue
answer //= gcdValue
print(str(answer) + "/" + str(total))