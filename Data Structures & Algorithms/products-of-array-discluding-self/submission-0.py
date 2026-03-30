class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productTotal = 1
        zeroCount = 0

        for num in nums:
            if num == 0:
                zeroCount += 1
                continue
            
            productTotal *= num

        if zeroCount > 1:
            return [0] * len(nums)

        res = []

        for num in nums:
            if num == 0:
                res.append(productTotal)
            elif zeroCount == 1:
                res.append(0)
            else:
                res.append(productTotal // num)

        return res