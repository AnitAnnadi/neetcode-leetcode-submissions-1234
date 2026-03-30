class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        prefix = []

        for num in nums:
            total += num
            prefix.append(total)

        postfix = [0] * len(nums)
        for i in range(len(nums)):
            postfix[i] = total
            total -= nums[i]

        for i in range(len(prefix)):
            if prefix[i] == postfix[i]:
                return i

        return -1



        