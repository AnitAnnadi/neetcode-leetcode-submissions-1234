class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        prefix = []
        cSum = 0
        for num in nums:
            cSum += num
            prefix.append(cSum)

        for i in range(n):
            if prefix[i] == k:
                count += 1
            elif prefix[i] != k:

                for j in range(0, i):
                    if prefix[i] - prefix[j] == k or prefix[i] + prefix[j] == k:
                        count +=1

        return count