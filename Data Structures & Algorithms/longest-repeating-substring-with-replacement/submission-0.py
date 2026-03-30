class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l, maxWindow = 0, 0

        for r in range(len(s)):
            counts[s[r]] += 1

            while ((r - l + 1) - max(counts.values())) > k:
                counts[l] -= 1
                l += 1
            
            maxWindow = max(maxWindow, r - l + 1)

        return maxWindow
