# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def goodNodesHelper(curr, maxVal):
            if not curr:
                return

            nonlocal res
            if curr.val >= maxVal:
                res += 1
            
            maxVal = max(maxVal, curr.val)
            goodNodesHelper(curr.left, maxVal)
            goodNodesHelper(curr.right, maxVal)

        goodNodesHelper(root, root.val)
        return res
            
