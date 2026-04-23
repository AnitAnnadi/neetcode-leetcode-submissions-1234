class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cLen = len(cost)
        if cLen == 2:
            return min(cost)
        
        dp = [0] * cLen
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, cLen):
            dp[i] = min(cost[i] + dp[i-1], cost[i] + dp[i-2])

        print(dp)

        return min(dp[cLen-1], dp[cLen-2])