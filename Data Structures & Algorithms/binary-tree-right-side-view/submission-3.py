# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()

        if root:
            q.append(root)

        while q:
            currNode = None
            for i in range(len(q)):
                currNode = q.popleft()

                if currNode.left:
                    q.append(currNode.left)
                
                if currNode.right:
                    q.append(currNode.right)
            
            res.append(currNode.val)
        
        return res