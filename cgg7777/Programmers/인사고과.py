def solution(scores):
    answer = 1

    newScores = scores[1:]
    newScores.sort(key=lambda x: (-x[0], x[1]))

    beforePeer = 0
    for newScore in newScores:
        if scores[0][0] < newScore[0] and scores[0][1] < newScore[1]:
            return -1
        # 5 4 -> 4 100 -> 3 101
        if beforePeer <= newScore[1]:
            beforePeer = newScore[1]
            if newScore[0] + newScore[1] > scores[0][0] + scores[0][1]:
                answer += 1

    return answer