class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = [0] * len(nums)
        maxS = 1

        for i in range(len(nums)):
            l[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    l[i] = max(l[i], 1 + l[j])
                    maxS = max(maxS, l[i])
        
        return maxS