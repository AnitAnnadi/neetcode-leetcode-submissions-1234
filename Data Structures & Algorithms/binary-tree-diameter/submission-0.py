# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]

            maxLPath, maxLeftPath = dfs(node.left)
            maxRPath, maxRightPath = dfs(node.right)

            maxPath = max(maxLPath, maxRPath, maxLeftPath + maxRightPath)

            return [maxPath, 1 + max(maxLeftPath, maxRightPath)]
            
        return dfs(root)[0]

        