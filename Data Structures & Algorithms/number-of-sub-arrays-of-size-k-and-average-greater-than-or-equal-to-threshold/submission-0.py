class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = 0
        count = 0
        l = 0

        for r in range(len(arr)):
            currSum += arr[r]

            if r + 1 >= k:
                count = count + 1 if currSum / k >= threshold else count
                currSum -= arr[l]
                l += 1
        
        return count