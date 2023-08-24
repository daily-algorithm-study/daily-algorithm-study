def possibleComb(leftValue, beforeValue, leftCount):
    answer = []
    if leftCount != 1:
        for i in range(beforeValue, leftValue + 1):
            if leftValue - i >= 1:
                tempLists = possibleComb(leftValue - i, 1, leftCount - 1)
                for tempList in tempLists:
                    answer.append([i] + tempList)
    else:
        answer.append([leftValue])
    return answer


def calculateWaitingTime(k, case, waitingQueue):
    processingQueue = [[0 for _ in range(case[i])] for i in range(len(case))]

    waitingTime = 0
    for i in range(0, k):
        for req in waitingQueue[i]:
            minWaitingTime = 10000000
            minIndex = 0
            insertFlag = False
            tmpWaitingTime = 0
            for j in range(0, len(processingQueue[i])):
                if processingQueue[i][j] <= req[0]:
                    processingQueue[i][j] = req[0] + req[1]
                    insertFlag = True
                    break
                else:
                    tmpWaitingTime = processingQueue[i][j] - req[0]
                    if tmpWaitingTime < minWaitingTime:
                        minWaitingTime = tmpWaitingTime
                        minIndex = j
            if not insertFlag:
                waitingTime += minWaitingTime
                processingQueue[i][minIndex] = processingQueue[i][minIndex] + req[1]

    return waitingTime


def solution(k, n, reqs):
    answer = 100000000
    waitingQueue = [[] for _ in range(k)]
    possibleCases = possibleComb(n, 1, k)
    for req in reqs:
        waitingQueue[req[2] - 1].append(req)
    for case in possibleCases:
        time = calculateWaitingTime(k, case, waitingQueue)
        if answer > time:
            answer = time
    return answer