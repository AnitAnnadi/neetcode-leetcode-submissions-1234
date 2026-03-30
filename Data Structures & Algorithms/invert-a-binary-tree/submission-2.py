# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q = deque()
        if root:
            q.append(root)

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                tmpPtr = curr.left
                curr.left = curr.right
                curr.right = tmpPtr

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

        return root