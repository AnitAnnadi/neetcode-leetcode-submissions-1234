class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next

        while curr:
            if i == index:
                return curr.val
            
            curr = curr.next
        
        return -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node

        if self.tail == self.head:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        prevNode = self.head
        i = 0

        while prevNode and i < index:
            prevNode = prevNode.next
            i += 1
        
        if prevNode and prevNode.next:
            if prevNode.next == self.tail:
                self.tail = prevNode
            
            prevNode.next = prevNode.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next

        while curr:
            values.append(curr.val)
            curr = curr.next
        
        return values
        
