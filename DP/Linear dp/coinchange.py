class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bottom-up DP for finding minimum coins to make amount.
        For each amount, try all coins and take minimum.
        
        Time: O(amount * coins), Space: O(amount)
        Recurrence: dp[a] = min(dp[a], 1 + dp[a-coin])
        Base case: dp[0] = 0
        """
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount] != amount+1 else -1