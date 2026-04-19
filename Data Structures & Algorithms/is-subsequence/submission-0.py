class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointer, tPointer = 0, 0

        while sPointer < len(s) and tPointer < len(t):
            if s[sPointer] == t[tPointer]:
                sPointer += 1

            tPointer += 1
        
        return True if sPointer == len(s) else False