class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word):
        curr = self.head

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.word = True
    
    def searchWord(self, word):
        curr = self.head

        for c in word:
            if c not in curr.children:
                return False
            
            curr = curr.children[c]
        
        return curr.word
    
    def searchPrefix(self, prefix):
        curr = self.head

        for c in prefix:
            if c not in curr.children:
                return False
            
            curr = curr.children[c]
        
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dictionary = Trie()
        for word in words:
            dictionary.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        visited = [[0] * ROWS for _ in range(COLS)]
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if visited[r][c] == 0:
                    self.dfsHelper(board, dictionary, visited, res, "", r, c)
        
        return res


    def dfsHelper(self, board, dictionary, visited, res, currWord, r, c):
        ROWS, COLS = len(board), len(board[0])

        if min(r, c) < 0 or r == ROWS or c == COLS or visited[r][c] == 1:
            return False
        
        currWord += board[r][c]
        if not dictionary.searchPrefix(currWord):
            return False
        
        visited[r][c] = 1
        keepMarkedAsVisited = False

        if (self.dfsHelper(board, dictionary, visited, res, currWord, r + 1, c) 
        or self.dfsHelper(board, dictionary, visited, res, currWord, r - 1, c) 
        or self.dfsHelper(board, dictionary, visited, res, currWord, r, c + 1) 
        or self.dfsHelper(board, dictionary, visited, res, currWord, r, c - 1)):
            keepMarkedAsVisited = True

        if dictionary.searchWord(currWord):
            res.append(currWord)
            return True
        
        if keepMarkedAsVisited:
            return True
        
        visited[r][c] = 0
        return False




