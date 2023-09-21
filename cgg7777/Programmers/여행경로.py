def solution(tickets):
    def DFS(path, visitedMap, tickets, count, answerCandidate):
        currentPath = path
        currentNode = currentPath[-1]

        if (count == len(tickets)):
            if len(answerCandidate) == 0:
                answerCandidate.append(currentPath)
            else:
                for i, entry in enumerate(answerCandidate[0]):
                    if entry > currentPath[i]:
                        answerCandidate[0] = currentPath
                        break
                    elif entry < currentPath[i]:
                        break
            return

        for ticket in tickets:
            if ticket[0] == currentNode and visitedMap[(ticket[0], ticket[1])] > 0:
                visitedMap[(ticket[0], ticket[1])] -= 1
                DFS(currentPath + [ticket[1]], visitedMap, tickets, count + 1, answerCandidate)
                visitedMap[(ticket[0], ticket[1])] += 1

    answerCandidate = []
    answer = []
    candidates = []
    visitedMap = {}
    for ticket in tickets:
        if (ticket[0], ticket[1]) in visitedMap:
            visitedMap[(ticket[0], ticket[1])] += 1
        else:
            visitedMap[(ticket[0], ticket[1])] = 1
        if (ticket[0] == "ICN"):
            candidates.append(ticket)

    for candidate in candidates:
        visitedMap[(candidate[0], candidate[1])] -= 1
        DFS(candidate, visitedMap, tickets, 1, answerCandidate)
        visitedMap[(candidate[0], candidate[1])] += 1

    answer = answerCandidate[0]
    return answer