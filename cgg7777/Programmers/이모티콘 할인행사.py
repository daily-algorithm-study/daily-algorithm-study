def solution(users, emoticons):
    def possibleCase(length):
        answerList = []
        if length != 1:
            for i in range(10, 41, 10):
                tempLists = possibleCase(length - 1)
                for tempList in tempLists:
                    answerList.append([i] + tempList)
        else:
            for i in range(10, 41, 10):
                answerList.append([i])
        return answerList

    answer = []

    answerList = []
    caseList = possibleCase(len(emoticons))
    for case in caseList:
        serviceJoin = 0
        profit = 0
        for user in users:
            totalPrice = 0
            for i in range(len(case)):
                if user[0] <= case[i]:
                    totalPrice += emoticons[i] * (100 - case[i]) // 100
            if totalPrice >= user[1]:
                serviceJoin += 1
            else:
                profit += totalPrice
        answerList.append([serviceJoin, profit])
    answerList.sort()
    answer = answerList[-1]
    return answer