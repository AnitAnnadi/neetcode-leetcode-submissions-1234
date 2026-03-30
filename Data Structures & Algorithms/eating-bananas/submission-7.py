class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minRate = r

        while l <= r:
            currRate = l + (r - l) // 2

            numHours = 0
            for pile in piles:
                numHours += math.ceil(pile / currRate)
            
            if numHours > h:
                l = currRate + 1
            else:
                minRate = currRate
                r = currRate - 1
        
        return minRate