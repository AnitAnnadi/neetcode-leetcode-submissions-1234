class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, maxLength = 0, 0

        for r in range(len(s)):
            if s[r] in chars:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
            
            chars.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength