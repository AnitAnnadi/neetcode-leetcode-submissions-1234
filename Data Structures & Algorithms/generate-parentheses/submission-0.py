class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, curr = [], []

        def generateParenthesisHelper(numOpen, numClose):
            if numOpen == 0 and numClose == 0:
                res.append("".join(curr))
            
            if numOpen != 0:
                curr.append("(")
                generateParenthesisHelper(numOpen - 1, numClose)
                curr.pop()

            if numOpen < numClose:
                curr.append(")")
                generateParenthesisHelper(numOpen, numClose - 1)
                curr.pop()
        
        generateParenthesisHelper(n, n)
        return res



