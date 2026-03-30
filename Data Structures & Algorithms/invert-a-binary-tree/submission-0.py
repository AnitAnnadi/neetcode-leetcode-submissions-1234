# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q = deque()
        nums = []

        if root:
            q.append(root)
            nums.append(root.val)

        while q:
            levelNums = []
            for i in range(len(q)):
                curr = q.popleft()
                curr.val = nums[-1]
                nums.pop()

                if curr.left:
                    levelNums.append(curr.left.val)
                    q.append(curr.left)

                if curr.right:
                    levelNums.append(curr.right.val)
                    q.append(curr.right)

            nums = levelNums
        return root
        