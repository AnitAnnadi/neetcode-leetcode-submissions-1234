# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        state = [k, None]

        def inOrder(root):
            if not root or state[0] == 0:
                return

            inOrder(root.left)

            state[0] -= 1
            if state[0] == 0:
                state[1] = root.val
            
            inOrder(root.right)
        
        inOrder(root)
        return state[1]
