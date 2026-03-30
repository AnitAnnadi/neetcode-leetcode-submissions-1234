# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque()
        if root:
            q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                currNode = q.popleft()
                level.append(currNode.val)

                if currNode.left:
                    q.append(currNode.left)
                
                if currNode.right:
                    q.append(currNode.right)
                
            if len(res) % 2:
                level.reverse()
            res.append(level)
        
        return res
            
