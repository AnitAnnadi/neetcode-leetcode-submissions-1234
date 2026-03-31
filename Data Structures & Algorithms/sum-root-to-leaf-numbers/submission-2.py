# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total, currNum = 0, 0

        def dfs(node):
            nonlocal total
            nonlocal currNum

            if not node:
                return

            currNum = currNum * 10 + node.val
            if not node.left and not node.right:
                total += currNum
                currNum //= 10
                return
            
            dfs(node.left)
            dfs(node.right)
            currNum //= 10

        dfs(root)
        return total