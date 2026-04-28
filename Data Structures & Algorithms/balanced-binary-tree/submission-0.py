# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]

        def dfs(node):
            if not node:
                return 0
            
            heightLeft = dfs(node.left)
            heightRight = dfs(node.right)

            if abs(heightRight - heightLeft) > 1:
                res[0] = False

            return 1 + max(heightLeft, heightRight)

        dfs(root)
        
        return res[0]
        
            
