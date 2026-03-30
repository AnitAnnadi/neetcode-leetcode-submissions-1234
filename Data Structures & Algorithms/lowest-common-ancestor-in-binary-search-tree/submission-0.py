# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pPath, qPath = [], []

        self.dfs(root, p, pPath)
        self.dfs(root, q, qPath)

        smaller, larger = [], []

        if len(pPath) < len(qPath):
            smaller = pPath
            larger = set(qPath)
        else:
            smaller = qPath
            larger = set(pPath)
        
        for i in range(len(smaller) - 1, -1, -1):
            if smaller[i] in larger:
                return smaller[i]
            
    def dfs(self, root, target, path):
        if not root:
            return False
        
        path.append(root)

        if root.val == target.val:
            return True

        if self.dfs(root.left, target, path) or self.dfs(root.right, target, path):
            return True

        path.pop()
        return False