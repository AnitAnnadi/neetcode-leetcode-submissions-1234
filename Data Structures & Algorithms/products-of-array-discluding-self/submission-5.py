class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]
        product = nums[0]

        for i in range(1, n):
            res.append(product)
            product *= nums[i]
        
        product = nums[n - 1]
        for i in range(n - 2, -1, -1):
            res[i] = res[i] * product
            product *= nums[i]

        return res
