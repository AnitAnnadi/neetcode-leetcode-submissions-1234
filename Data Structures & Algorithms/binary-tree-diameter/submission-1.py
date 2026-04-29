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

            leftDiameter, leftHeight = dfs(node.left)
            rightDiameter, rightHeight = dfs(node.right)

            diameter = max(leftDiameter, rightDiameter, leftHeight + rightHeight)
            height = 1 + max(leftHeight, rightHeight)

            return [diameter, height]

        return dfs(root)[0]

        