# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = [0]
        currNum = []

        def dfs(node):
            if not node:
                return

            currNum.append(str(node.val))
            if not node.left and not node.right:
                total[0] += int("".join(currNum))
                currNum.pop()
                return
            
            dfs(node.left)
            dfs(node.right)
            currNum.pop()

        dfs(root)
        return total[0]