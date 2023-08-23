import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        parsedArr = re.findall("[^/]+|\/", path)
        stack = []
        for entry in parsedArr:
            if entry == "..":
                if len(stack) >=2:
                    stack.pop()
                    stack.pop()
            elif entry == ".":
                continue
            elif entry == "/":
                if stack and stack[-1] == "/":
                    continue
                else:
                    stack.append(entry)
            else:
                stack.append(entry)
        if stack[-1] == "/" and len(stack) >=2:
            stack.pop()
        return ''.join(stack)
