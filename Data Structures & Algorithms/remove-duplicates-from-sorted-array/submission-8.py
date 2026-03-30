class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for i in range(l, len(nums)):

            if nums[i] != nums[i - 1]:
                nums[l] = nums[i]
                l += 1

        return l