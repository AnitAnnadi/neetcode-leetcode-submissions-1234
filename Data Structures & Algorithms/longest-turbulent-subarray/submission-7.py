class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        count = 1
        prev = ""

        while r < len(arr):
            if arr[r - 1] < arr[r] and prev != "<":
                count = max(count, r - l + 1)
                r += 1
                prev = "<"
            elif arr[r - 1] > arr[r] and prev != ">":
                count = max(count, r - l + 1)
                r += 1
                prev = ">"
            else:
                r = r + 1 if arr[r - 1] == arr[r] else r
                l = r - 1
                prev = ""

        return count

            