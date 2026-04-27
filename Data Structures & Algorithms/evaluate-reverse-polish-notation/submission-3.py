class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            operand = token == "+" or token == "-" or token == "*" or token == "/"

            res = token
            if operand:
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                if token == "+":
                    res = num1 + num2
                elif token == "-":
                    res = num2 - num1
                elif token == "*":
                    res = num1 * num2
                else:
                    res = math.trunc(num2 / num1)

            stack.append(str(res))

        return int(stack[0])

