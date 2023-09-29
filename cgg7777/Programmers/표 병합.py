def solution(commands):
    def find(parent, pos):
        x = pos[0]
        y = pos[1]
        if parent[x][y] == (x, y):
            return (x, y)
        else:
            return find(parent, parent[x][y])

    def union(parent, board, pos1, pos2):

        posParent1 = find(parent, pos1)
        posParent2 = find(parent, pos2)

        if posParent1 == posParent2:
            return

        if board[posParent1[0]][posParent1[1]] is not None:
            parent[posParent2[0]][posParent2[1]] = posParent1
        else:
            parent[posParent1[0]][posParent1[1]] = posParent2

    answer = []

    board = [[None for _ in range(50)] for i in range(50)]
    parent = [[(i, j) for j in range(50)] for i in range(50)]

    mergeKey = 1

    mergeKeyToValue = {}
    mergeKeyToSet = {}
    for command in commands:
        commandArr = command.split(' ')
        if (commandArr[0] == "UPDATE"):
            if (len(commandArr) == 4):
                x = int(commandArr[1]) - 1
                y = int(commandArr[2]) - 1

                findResult = find(parent, (x, y))

                parentX = findResult[0]
                parentY = findResult[1]

                for i in range(50):
                    for j in range(50):
                        if find(parent, (i, j)) == (parentX, parentY):
                            board[i][j] = commandArr[3]
            else:
                for i in range(50):
                    for j in range(50):
                        if board[i][j] == commandArr[1]:
                            board[i][j] = commandArr[2]

        elif (commandArr[0] == "MERGE"):
            x1 = int(commandArr[1]) - 1
            y1 = int(commandArr[2]) - 1

            x2 = int(commandArr[3]) - 1
            y2 = int(commandArr[4]) - 1

            union(parent, board, (x1, y1), (x2, y2))

        elif commandArr[0] == "UNMERGE":
            x = int(commandArr[1]) - 1
            y = int(commandArr[2]) - 1

            commonParent = find(parent, (x, y))
            commonValue = board[commonParent[0]][commonParent[1]]

            unmergeSet = set()
            for i in range(50):
                for j in range(50):
                    if find(parent, (i, j)) == commonParent:
                        board[i][j] = None
                        unmergeSet.add((i, j))

            for pos in unmergeSet:
                parent[pos[0]][pos[1]] = (pos[0], pos[1])

            board[x][y] = commonValue

        elif commandArr[0] == "PRINT":
            x = int(commandArr[1]) - 1
            y = int(commandArr[2]) - 1
            targetParent = find(parent, (x, y))
            if board[targetParent[0]][targetParent[1]] is None:
                answer.append("EMPTY")
            else:
                answer.append(board[targetParent[0]][targetParent[1]])

    return answer