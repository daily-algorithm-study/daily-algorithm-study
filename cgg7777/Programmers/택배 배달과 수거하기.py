def solution(cap, n, deliveries, pickups):
    answer = -1
    deliverArr = [[i, deliveries[i]] for i in range(len(deliveries))]
    pickArr = [[i, pickups[i]] for i in range(len(deliveries))]
    while deliverArr and deliverArr[-1][1] == 0:
        deliverArr.pop()
    while pickArr and pickArr[-1][1] == 0:
        pickArr.pop()

    dist = 0
    while deliverArr or pickArr:
        farthestHome = max(len(deliverArr), len(pickArr))
        dist += farthestHome * 2

        howManyPick = cap
        howManyReturn = cap

        while deliverArr:
            current = deliverArr[-1]
            if current[1] > howManyPick:
                current[1] -= howManyPick
                break
            else:
                howManyPick -= current[1]
                deliverArr.pop()

        while pickArr:
            current = pickArr[-1]
            if current[1] > howManyReturn:
                current[1] -= howManyReturn
                break
            else:
                howManyReturn -= current[1]
                pickArr.pop()

    answer = dist
    return answer