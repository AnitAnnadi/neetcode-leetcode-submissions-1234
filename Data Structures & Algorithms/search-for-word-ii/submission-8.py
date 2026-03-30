class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word):
        curr = self.head

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dictionary = Trie()
        for word in words:
            dictionary.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                self.dfsHelper(board, res, dictionary.head, r, c)
        
        return res


    def dfsHelper(self, board, res, TrieNode, r, c):
        ROWS, COLS = len(board), len(board[0])
        char = board[r][c]

        if char not in TrieNode.children:
            return

        nextTrieNode = TrieNode.children[char]
        if nextTrieNode.word:
            res.append(nextTrieNode.word)
            nextTrieNode.word = None
        

        board[r][c] = "#"

        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            newR, newC = r + dr, c + dc
            if min(newR, newC) < 0 or newR == ROWS or newC == COLS or board[newR][newC] == "#":
                continue
            
            self.dfsHelper(board, res, nextTrieNode, newR, newC)
        
        board[r][c] = char

        if nextTrieNode.word:
            TrieNode.children.pop(char)