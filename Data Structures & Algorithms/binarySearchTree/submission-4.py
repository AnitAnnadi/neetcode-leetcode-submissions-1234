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
        curr = self.root

        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        
        minNode = self.getMinHelper(self.root)
        return minNode.val

    def getMax(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr and curr.right:
            curr = curr.right
        
        return curr.val


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
        else:
            curr.val = val

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

