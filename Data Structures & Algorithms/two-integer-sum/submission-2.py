class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        for i, num in enumerate(nums):
            rem = target - num

            if rem in myDict:
                return [myDict[rem], i]
            
            myDict[num] = i