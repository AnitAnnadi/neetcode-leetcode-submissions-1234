class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = []
        postfix = [0] * n

        product = 1

        for num in nums:
            product *= num
            prefix.append(product)

        product = 1
        for i in range(n - 1, -1, -1):
            product *= nums[i]
            postfix[i] = product

        res = []
        for i in range(n):
            leftProduct = prefix[i - 1] if i - 1 >= 0 else 1
            rightProduct = postfix[i + 1] if i + 1 < n else 1

            res.append(leftProduct * rightProduct)
        
        return res