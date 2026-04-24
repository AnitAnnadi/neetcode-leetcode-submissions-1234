class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if strs == [""]:
            return "é"

        return "中".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        if s == "é":
            return [""]

        return s.split("中")