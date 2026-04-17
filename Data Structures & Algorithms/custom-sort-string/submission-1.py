class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = [0] * 26
        res = []

        for c in s:
            idx = ord(c) - ord('a')
            counts[idx] += 1
        
        for c in order:
            idx = ord(c) - ord('a')
            while counts[idx] > 0:
                res.append(c)
                counts[idx] -= 1

        for idx in range(26):
            c = chr(idx + ord('a'))
            while counts[idx] > 0:
                res.append(c)
                counts[idx] -= 1
        
        return "".join(res)
        
        