class ListNode:
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.myDict = {}
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.myDict:
            self.removeNode(self.myDict[key])
            self.addNode(self.myDict[key])

            return self.myDict[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.myDict:
            self.myDict[key].val = value
            self.removeNode(self.myDict[key])
            self.addNode(self.myDict[key])
        else:
            newNode = ListNode(key, value)
            self.myDict[key] = newNode
            self.addNode(newNode)

        if len(self.myDict) > self.capacity:
            self.myDict.pop(self.head.next.key)
            self.removeNode(self.head.next)
    
    def addNode(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    def removeNode(self, node):
        node.next.prev = node.prev  
        node.prev.next = node.next      
