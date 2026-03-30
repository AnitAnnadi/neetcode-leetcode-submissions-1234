# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeListsHelper(lists, 0, len(lists) - 1)
    
    def mergeListsHelper(self, lists, s, e):
        if s > e:
            return None
        
        if s == e:
            return lists[s]

        m = s + (e - s) // 2
        left = self.mergeListsHelper(lists, s, m)
        right = self.mergeListsHelper(lists, m + 1, e)

        return self.merge(left, right)
    
    def merge(self, left, right):
        dummy = node = ListNode(-1)

        while left and right:
            if left.val <= right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        
        if left:
            node.next = left
        else:
            node.next = right

        return dummy.next




