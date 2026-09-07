class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        cProd = 1
        for i in range(len(nums)):
            res[i] = cProd
            cProd *= nums[i]

        cProd = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= cProd
            cProd *= nums[i]

        return res
        