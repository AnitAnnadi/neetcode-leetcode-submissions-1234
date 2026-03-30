class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]

        curr.word = True

    def search(self, word: str) -> bool:
        return self.searchHelper(word, 0, self.head)
    
    def searchHelper(self, word, i, TrieNode):
        if len(word) == i:
            return TrieNode.word

        char = word[i]
        if char == ".":
            for node in TrieNode.children.values():
                if self.searchHelper(word, i + 1, node):
                    return True
            
            return False

        if char not in TrieNode.children:
            return False
        
        return self.searchHelper(word, i + 1, TrieNode.children[char])
        
