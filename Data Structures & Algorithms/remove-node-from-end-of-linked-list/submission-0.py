# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        count = 0
        tmpPtr = head
        while tmpPtr:
            count += 1
            tmpPtr = tmpPtr.next

        nodeNum = count - n - 1
        tmpPtr2 = head

        if nodeNum < 0:
            return head.next

        for i in range(nodeNum):
            tmpPtr2 = tmpPtr2.next
        
        tmpPtr2.next = tmpPtr2.next.next
        return head