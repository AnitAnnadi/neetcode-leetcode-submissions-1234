class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxContainer = 0

        while l < r:
            minBar = min(heights[l], heights[r])
            maxContainer = max(maxContainer, minBar * (r - l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxContainer

