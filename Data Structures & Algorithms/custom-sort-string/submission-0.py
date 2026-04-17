class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = defaultdict(int)
        res = []

        for c in s:
            counts[c] += 1
        
        for c in order:
            if c in counts:
                while counts[c] > 0:
                    res.append(c)
                    counts[c] -= 1

        for c in counts:
            while counts[c] > 0:
                    res.append(c)
                    counts[c] -= 1
        
        return "".join(res)
        
        