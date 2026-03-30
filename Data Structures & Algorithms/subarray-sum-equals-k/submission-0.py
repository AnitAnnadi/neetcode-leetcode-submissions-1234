class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = []
        postfix = [0] * n
        count = 0

        cSum = 0
        for num in nums:
            cSum += num
            prefix.append(cSum)

        cSum = 0
        for i in range(n - 1, -1, -1):
            cSum += nums[i]
            postfix[i] = cSum
        
        for i in range(n):
            if nums[i] == k or prefix[i] == k or postfix[i] == k:
                count += 1
            
        return count