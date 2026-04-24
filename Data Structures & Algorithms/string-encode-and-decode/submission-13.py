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
            while i < len(s) and s[i] != "#":
                wordLen.append(s[i])
                i += 1
            
            i += 1
            print("".join(wordLen))
            wordLen = int("".join(wordLen))

            currWord = []
            while i < len(s) and wordLen > 0:
                currWord.append(s[i])
                wordLen -= 1
                i += 1
            currWord = "".join(currWord)
            res.append(currWord)

        return res