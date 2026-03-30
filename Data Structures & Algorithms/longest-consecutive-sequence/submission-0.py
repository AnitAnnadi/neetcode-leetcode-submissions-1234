class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        visited = set()
        maxSeq = 1

        for num in nums:
            if num in visited:
                continue

            currNum = num + 1
            currSeq = 1
            while currNum in nums:
                currSeq += 1
                visited.add(currNum)
                currNum += 1

            currNum = num - 1
            while currNum in nums:
                currSeq -= 1
                visited.add(currNum)
                currNum -= 1
            
            maxSeq = max(currSeq, maxSeq)
        
        return maxSeq
            
