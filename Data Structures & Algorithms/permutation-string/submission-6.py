class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countsS1, countsS2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            countsS1[ord(s1[i]) - ord('a')] += 1
            countsS2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(len(countsS1)):
            if countsS1[i] == countsS2[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idxR = ord(s2[r]) - ord('a')
            countsS2[idxR] += 1

            if countsS1[idxR] == countsS2[idxR]:
                matches += 1
            elif countsS1[idxR] == countsS2[idxR] - 1:
                matches -= 1

            idxL = ord(s2[l]) - ord('a')
            countsS2[idxL] -= 1

            if countsS1[idxL] == countsS2[idxL]:
                matches += 1
            elif countsS1[idxL] == countsS2[idxL] + 1:
                matches -= 1

            l += 1
        
        return matches == 26


