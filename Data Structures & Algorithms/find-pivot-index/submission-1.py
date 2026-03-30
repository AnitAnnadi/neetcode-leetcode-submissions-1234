class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        prefix = []

        for num in nums:
            total += num
            prefix.append(total)

        for i in range(len(prefix)):
            rSum = prefix[-1] - (prefix[i - 1] if i > 0 else 0)
            if prefix[i] == rSum:
                return i

        return -1



        