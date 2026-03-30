# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        self.inOrderTraversalHelper(root, traversal)
        return traversal


    def inOrderTraversalHelper(self, root, traversal):
        if not root:
            return

        self.inOrderTraversalHelper(root.left, traversal)
        traversal.append(root.val)
        self.inOrderTraversalHelper(root.right, traversal)