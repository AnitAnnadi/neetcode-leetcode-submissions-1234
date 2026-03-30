class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node = ListNode(value)

        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def appendleft(self, value: int) -> None:
        node = ListNode(value)

        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        nodeToRemove = self.tail.prev
        nodeToRemove.prev.next = nodeToRemove.next
        nodeToRemove.next.prev = nodeToRemove.prev

        return nodeToRemove.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        nodeToRemove = self.head.next
        nodeToRemove.prev.next = nodeToRemove.next
        nodeToRemove.next.prev = nodeToRemove.prev

        return nodeToRemove.val
