class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                diff = i - coin
                if diff >= 0 and dp[diff] >= 0:

                    if dp[i] == -1:
                        dp[i] = 1 + dp[diff]
                    else:
                        dp[i] = min(dp[i], 1 + dp[diff])

        return dp[-1]