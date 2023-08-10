class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        numArr = [i + 1 for i in range(n)]

        def recursiveCombine(arr, lastPickedIndex, depth):
            if depth == k:
                return arr

            accArr = []
            for i, num in enumerate(numArr):
                if i > lastPickedIndex:
                    if depth == k - 1:
                        accArr.append(recursiveCombine(arr + [num], i, depth + 1))
                    else:
                        accArr += recursiveCombine(arr + [num], i, depth + 1)
            return accArr

        numArr = [i + 1 for i in range(n)]
        return recursiveCombine([], -1, 0)