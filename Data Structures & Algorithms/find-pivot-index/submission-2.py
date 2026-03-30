class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        total = 0

        for num in nums:
            total += num
            prefix.append(total)

        for i in range(1, len(prefix)):
            leftSum = prefix[i - 1]
            rightSum = prefix[len(prefix) - 1] - prefix[i]

            if leftSum == rightSum:
                return i - 1
        
        return -1
