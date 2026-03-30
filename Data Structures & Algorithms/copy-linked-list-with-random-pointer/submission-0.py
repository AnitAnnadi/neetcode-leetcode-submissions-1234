"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        dummyHead = Node(0)
        curr = dummyHead

        while head:
            if head.val not in nodes:
                nodes[head.val] = Node(head.val)

            if head.random and head.random.val not in nodes:
                nodes[head.random.val] = Node(head.random.val)

            curr.next = nodes[head.val]

            if head.random:
                curr.next.random = nodes[head.random.val]

            head = head.next
            curr = curr.next
        
        return dummyHead.next