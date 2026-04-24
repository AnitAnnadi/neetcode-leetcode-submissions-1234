class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = f"{len(strs[i])}#" + strs[i]
        
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            wordLen = int(s[i:j])
            currWord = s[j + 1 : j + 1 + wordLen]
            res.append(currWord)

            i = j + 1 + wordLen

        return res