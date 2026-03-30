class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            "[": "]",
            "{": "}",
            "(": ')'
        }

        for c in s:
            if c in parentheses:
                stack.append(c)
            else:
                if stack and parentheses[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
