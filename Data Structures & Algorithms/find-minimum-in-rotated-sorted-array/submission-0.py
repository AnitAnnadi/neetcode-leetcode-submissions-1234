class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[l] < nums[r]:
                r = mid - 1
            elif nums[l] > nums[r]:
                l = mid + 1
            else:
                break
        
        if l > 0:
            return nums[l-1]
        
        return nums[l]
            