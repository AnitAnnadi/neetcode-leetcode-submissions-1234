class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:

            letters = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                letters[idx] += 1

            letters = tuple(letters)
            res[letters].append(word)
        
        return list(res.values())