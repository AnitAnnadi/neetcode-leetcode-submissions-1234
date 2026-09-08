# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        def maxDepthHelper(curr, depth):
            nonlocal res
            if not curr:
                return

            depth += 1
            res = max(res, depth)

            maxDepthHelper(curr.left, depth)
            maxDepthHelper(curr.right, depth)

        maxDepthHelper(root, 0)
        return res