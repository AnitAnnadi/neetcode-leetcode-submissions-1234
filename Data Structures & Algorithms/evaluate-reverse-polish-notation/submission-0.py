class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        currNum = int(tokens[0])

        for i in range(2, len(tokens), 2):
            secondNum = int(tokens[i - 1])
            op = tokens[i]

            if op == "+": currNum += secondNum
            elif op == "-": currNum -= secondNum
            elif op == "*": currNum *= secondNum
            else: currNum /= secondNum
        
        return currNum
