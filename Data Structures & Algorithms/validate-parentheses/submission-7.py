class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            "[": "]",
            "{": "}",
            "(": ')'
        }

        stack = []

        for c in s:
            if c in parenthesis:
                stack.append(c)
            else:
                if stack and parenthesis[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
