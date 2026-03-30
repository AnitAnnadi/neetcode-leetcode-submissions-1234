class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        vals = set()

        for num in nums:
            if num in vals:
                return num
            
            vals.add(num)

        return 0