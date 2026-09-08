# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def isBalancedHelper(curr):
            nonlocal res
            if not curr:
                return 0

            left = isBalancedHelper(curr.left)
            right = isBalancedHelper(curr.right)

            if abs(left - right) > 1:
                res = False
                return -1

            return 1 + max(left, right)
        
        isBalancedHelper(root)
        return res
