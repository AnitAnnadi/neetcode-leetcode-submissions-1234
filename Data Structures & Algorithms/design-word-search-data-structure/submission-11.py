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

    def searchHelper(self, word, i, curr):
        if len(word) == i:
            return curr.word

        c = word[i]
        if c == ".":
            for node in curr.children.values():
                if self.searchHelper(word, i + 1, node):
                    return True

            return False
        
        if c not in curr.children:
            return False
        
        return self.searchHelper(word, i + 1, curr.children[c])


        
