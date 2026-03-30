class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
    
    def hashFn(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        i = self.hashFn(key)
        prev = None
        curr = self.table[i]

        if not curr:
            self.table[i] = ListNode(key, value)
        else:
            while curr:
                if key == curr.key:
                    curr.val = value
                    return

                prev = curr
                curr = curr.next

            prev.next = ListNode(key, value)

        self.size += 1
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        i = self.hashFn(key)
        curr = self.table[i]

        while curr:
            if key == curr.key:
                return curr.val
            
            curr = curr.next

        return -1

    def remove(self, key: int) -> bool:
        i = self.hashFn(key)
        prev = None
        curr = self.table[i]

        while curr:
            if key == curr.key:
                if not prev:
                    self.table[i] = curr.next
                else:
                    prev.next = curr.next
                
                self.size -= 1
                return True
            
            prev = curr
            curr = curr.next
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        tmpTable = self.table
        self.capacity = self.capacity * 2
        self.size = 0
        self.table = [None] * self.capacity

        for node in tmpTable:
            while node:
                self.insert(node.key, node.val)
                node = node.next

