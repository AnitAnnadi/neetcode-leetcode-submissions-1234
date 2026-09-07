class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxStore, currStore = 0, 0

        while l < r:
            width = r - l
            currStore = width * min(heights[l], heights[r])
            maxStore = max(maxStore, currStore)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxStore
