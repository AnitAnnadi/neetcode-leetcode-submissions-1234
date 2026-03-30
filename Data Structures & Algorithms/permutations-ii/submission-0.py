class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums)
    
    def helper(self, i, nums):
        if i == len(nums) - 1:
            return [[nums[i]]]

        resPerms = []
        perms = self.helper(i + 1, nums)

        duplicate = nums[i] == nums[i + 1]

        for p in perms:

            if duplicate:
                pCopy = p.copy()
                pCopy.insert(0, nums[i])
                resPerms.append(pCopy)

                if p[0] != nums[i]:
                    pCopy2 = p.copy()
                    pCopy2.insert(1, nums[i])
                    resPerms.append(pCopy2)
            else:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, nums[i])
                    resPerms.append(pCopy)
        
        return resPerms