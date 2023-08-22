class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = [set() for _ in range(9)]
        columnCheck = [set() for _ in range(9)]
        rectangleCheck = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] in rowCheck[i]:
                        return False
                    else:
                        rowCheck[i].add(board[i][j])

                    if board[i][j] in columnCheck[j]:
                        return False
                    else:
                        columnCheck[j].add(board[i][j])

                    if board[i][j] in rectangleCheck[(i//3)*3 + (j//3)]:
                        return False
                    else:
                        rectangleCheck[(i//3)*3 + (j//3)].add(board[i][j])
        return True