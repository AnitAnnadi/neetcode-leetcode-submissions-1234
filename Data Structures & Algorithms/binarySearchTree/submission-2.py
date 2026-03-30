class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        self.root = self.insertHelper(self.root, key, val)

    def get(self, key: int) -> int:
        currNode = self.root

        while currNode:
            if key < currNode.key:
                currNode = currNode.left
            elif key > currNode.key:
                currNode = currNode.right
            else:
                return currNode.val
        
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        
        minNode = self.getMinHelper(self.root)
        return minNode.val

    def getMax(self) -> int:
        if not self.root:
            return -1

        currNode = self.root
        while currNode and currNode.right:
            currNode = currNode.right
        
        return currNode.val


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def getInorderKeys(self) -> List[int]:
        res = []
        self.inorder(self.root, res)
        return res
    
    def insertHelper(self, curr, key, val):
        if not curr:
            return ListNode(key, val)
        
        if key < curr.key:
            curr.left = self.insertHelper(curr.left, key, val)
        elif key > curr.key:
            curr.right = self.insertHelper(curr.right, key, val)
        
        return curr
    
    def getMinHelper(self, curr):
        while curr and curr.left:
            curr = curr.left
        
        return curr
    
    def removeHelper(self, curr, key):
        if not curr:
            return curr
        
        if key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        elif key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                minNode = self.getMinHelper(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
            
        return curr
    
    def inorder(self, curr, res):
        if not curr:
            return

        self.inorder(curr.left, res)
        res.append(curr.key)
        self.inorder(curr.right, res)

