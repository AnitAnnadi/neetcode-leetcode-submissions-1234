class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letterCounts = {}
        res = []

        for word in strs:

            letters = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                letters[idx] += 1

            letters = tuple(letters)
            
            if letters in letterCounts:
                res[letterCounts[letters]].append(word)
            else:
                res.append([word])
                letterCounts[letters] = len(res) - 1
        
        return res