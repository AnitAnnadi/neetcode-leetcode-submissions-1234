class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        maxLen = 0

        l, r = 0, 0
        for r in range(len(s)):
            if s[r] not in chars:
                chars.add(s[r])
                maxLen = max(maxLen, r - l + 1)
                continue

            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])

        return maxLen