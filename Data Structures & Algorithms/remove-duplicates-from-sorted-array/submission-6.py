class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        # loop through nums and place non-duplicates at the beginning
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                r += 1

        return l