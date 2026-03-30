class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 1 and strs[0] == "":
            return "edge"

        return "#######".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        elif s == "edge":
            return [""]

        return s.split("#######")