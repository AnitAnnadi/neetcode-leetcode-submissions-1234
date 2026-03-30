class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[l] < nums[r]:
                r = mid
            elif nums[l] > nums[r]:
                l = mid
            else:
                break
        
        if l > 0:
            return min(nums[l-1], nums[l])
        
        return nums[l]
            