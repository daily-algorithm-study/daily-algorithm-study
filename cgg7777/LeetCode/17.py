class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def recursiveMatch(depth):
            if depth == len(listedDigits):
                return [""]
            currentList = []
            beforeList = recursiveMatch(depth + 1)
            for entry in possibleLetters[int(listedDigits[depth])]:
                for before in beforeList:
                    currentList.append(entry + before)
            return currentList

        possibleLetters = {2: {"a", "b", "c"}, 3: {"d", "e", "f", }, 4: {"g", "h", "i"}, 5: {"j", "k", "l"},
                        6: {"m", "n", "o"}, 7: {"p", "q", "r", "s"}, 8: {"t", "u", "v"}, 9: {"w", "x", "y", "z"}}
        listedDigits : list[str] = list(digits)
        answer = recursiveMatch(0)
        if len(answer) == 1 and answer[0] == "":
            return []
        return answer

