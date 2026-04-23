class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cLen = len(cost)        
        val1 = cost[0]
        val2 = cost[1]

        for i in range(2, cLen):
            tmp = val2
            val2 = cost[i] + min(val1, val2)
            val1 = tmp

        return min(val1, val2)