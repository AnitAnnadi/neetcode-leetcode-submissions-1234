class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        # loop through nums and place elements that are not val at beginning
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        
        return l