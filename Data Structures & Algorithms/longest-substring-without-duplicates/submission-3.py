class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, maxLength = 0, 0

        for r in range(len(s)):
            if s[r] in chars:
                while s[l] != s[r]:
                    chars.remove(s[l])
                    l += 1
                l += 1
            else:
                maxLength = max(maxLength, r - l + 1)
                chars.add(s[r])

        return maxLength
