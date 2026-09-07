class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = {num for num in nums}
        res = 0

        for num in nums:
            count = 0
            if num - 1 not in mySet:
                curr = num
                while curr in mySet:
                    curr += 1
                    count += 1

            res = max(res, count)

        return res


        