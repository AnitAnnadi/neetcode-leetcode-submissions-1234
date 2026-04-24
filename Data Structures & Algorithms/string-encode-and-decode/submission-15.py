class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = f"{len(strs[i])}#" + strs[i]
        
        return "".join(strs)


    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            wordLen = []
            while s[i] != "#":
                wordLen.append(s[i])
                i += 1

            wordLen = int("".join(wordLen))
            i += 1

            currWord = s[i:i+wordLen]
            res.append(currWord)
            i += wordLen

        return res