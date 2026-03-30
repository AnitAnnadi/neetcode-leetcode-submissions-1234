# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = [0, 0]
        self.maxDepthHelper(root, res)

        return res[1]
        
    def maxDepthHelper(self, root, res):
        if not root:
            return
        
        res[0] += 1
        self.maxDepthHelper(root.left, res)

        if res[0] > res[1]:
            res[1] = res[0]

        self.maxDepthHelper(root.right, res)
        res[0] -= 1


        