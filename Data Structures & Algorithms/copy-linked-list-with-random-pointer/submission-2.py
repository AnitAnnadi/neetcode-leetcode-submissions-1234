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
        nodes = {None: None}
        dummyHead = Node(0)
        curr = dummyHead

        while head:
            if head not in nodes:
                nodes[head] = Node(head.val)

            if head.random and head.random not in nodes:
                nodes[head.random] = Node(head.random.val)

            curr.next = nodes[head]
            if head.random:
                curr.next.random = nodes[head.random]

            head = head.next
            curr = curr.next
        
        return dummyHead.next