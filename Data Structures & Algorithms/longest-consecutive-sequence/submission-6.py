class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        visited = set()
        maxSeq = 0

        for num in numsSet:
            if num in visited:
                continue

            currNum = num + 1
            currSeq = 1
            while currNum in numsSet:
                currSeq += 1
                visited.add(currNum)
                currNum += 1

            currNum = num - 1
            while currNum in numsSet:
                currSeq += 1
                visited.add(currNum)
                currNum -= 1
            
            maxSeq = max(currSeq, maxSeq)
        
        return maxSeq
            
