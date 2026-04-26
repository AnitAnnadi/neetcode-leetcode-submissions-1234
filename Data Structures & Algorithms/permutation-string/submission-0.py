class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use array of size 26 to have character count for s1
        # have an character count array for s2 that counts characters
        # using sliding window. The window size is of len(s1).

        if len(s2) < len(s1):
            return False

        countsS1, countsS2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            idxS1 = ord(s1[i]) - ord('a')
            countsS1[idxS1] += 1

            if i == len(s1) - 1:
                continue

            idxS2 = ord(s2[i]) - ord('a')
            countsS2[idxS2] += 1
        
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            idxR = ord(s2[r]) - ord('a')
            countsS2[idxR] += 1

            if countsS1 == countsS2:
                return True

            idxL = ord(s2[l]) - ord('a')
            countsS2[idxL] -= 1
            l += 1
        
        return False


