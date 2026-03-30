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

        for i in range(len(nums)):
            if zeroCount:
                nums[i] = 0 if nums[i] != 0 else productTotal
            else:
                nums[i] = productTotal // nums[i]

        return nums