import sys

# m : 10
# n: 10^4
# 10^7
def makePrimeArr():
    isPrime = [True] * 10000000
    for i in range(2, len(isPrime)):
        if not isPrime[i]: continue

        for j in range(i*2, len(isPrime), i):
            isPrime[j] = False

    primeArr = []
    for i in range(2, len(isPrime)):
        if isPrime[i]:
            primeArr.append(i)
    return isPrime, primeArr


T = int(sys.stdin.readline())
isPrime, primeArr = makePrimeArr()
intersection = set()
for i in range(T):
    m = int(sys.stdin.readline())
    nArr = list(map(int, sys.stdin.readline().split()))
    intersection = set()
    for j in range(len(nArr)):
        tempIntersection = set()
        rangeValue = nArr[j]
        sumValue = sum(primeArr[:rangeValue])
        if sumValue >= 9999999:
            continue
        if isPrime[sumValue]:
            tempIntersection.add(sumValue)
        for k in range(1, len(primeArr)-rangeValue+1):
            sumValue = sumValue - primeArr[k-1] + primeArr[k + rangeValue -1]
            if sumValue >= 9999999:
                continue
            if isPrime[sumValue]:
                tempIntersection.add(sumValue)
        if j == 0:
            intersection |= tempIntersection
        else:
            intersection &= tempIntersection
    commonList = list(intersection)
    commonList.sort()
    print("Scenario "+str(i+1)+":")
    print(commonList[0], end="\n\n")





