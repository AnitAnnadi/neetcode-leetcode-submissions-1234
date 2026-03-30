class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        i = 0
        while i < len(nums):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    prevNum = nums[l]
                    while l < r and nums[l] == prevNum:
                        l += 1
            
            prevNum = nums[i]
            while i < len(nums) and nums[i] == prevNum:
                i += 1
        
        return res
