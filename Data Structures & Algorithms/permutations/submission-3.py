class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        resPerms = [[]]

        for n in nums:
            perms = []

            for p in resPerms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    perms.append(pCopy)

            resPerms = perms
        
        return resPerms