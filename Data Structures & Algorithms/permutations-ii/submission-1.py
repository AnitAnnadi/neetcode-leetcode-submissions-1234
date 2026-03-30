class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums)
    
    def helper(self, i, nums):
        if i == len(nums) - 1:
            return [[nums[i]]]

        resPerms = []
        perms = self.helper(i + 1, nums)

        for p in perms:
            for j in range(len(p) + 1):
                if j > 0 and nums[i] == p[j-1]:
                    break

                pCopy = p.copy()
                pCopy.insert(j, nums[j])
                resPerms.append(pCopy)
        
        return resPerms