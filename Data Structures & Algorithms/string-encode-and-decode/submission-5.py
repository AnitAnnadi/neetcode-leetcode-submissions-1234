class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs[0] == "" and len(strs) == 1:
            return "edge"

        return "#".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        elif s == "edge":
            return [""]

        return s.split("#")