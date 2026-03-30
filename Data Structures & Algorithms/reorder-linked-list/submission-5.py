# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse the list from the middle node to the last node
        # now there are two pointers: head and tail
        # to construct new list add the node at head then the node at tail
        # move to the next node for both head and tail
        # repeat until there are no more nodes left to 

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None

        prev = None
        nextNode = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        tail = prev
        tmpPtr3 = head
        head = head.next

        while tail:
            tmpPtr3.next = tail
            tail = tail.next
            tmpPtr3 = tmpPtr3.next

            if head:
                tmpPtr3.next = head
                head = head.next
                tmpPtr3 = tmpPtr3.next