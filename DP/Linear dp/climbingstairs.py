class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Top-down memoization approach for climbing stairs.
        At each step, we can either take 1 step or 2 steps.
        
        Time: O(n), Space: O(n)
        Recurrence: f(i) = f(i+1) + f(i+2)
        Base case: f(n) = 1, f(n+1) = 0
        """
        dp = {}
        def dfs(i):
            if i >= n:
                if i == n:
                    return 1
                return 0
            if i in dp:
                return dp[i]
            dp[i] = dfs(i+1) + dfs(i+2)
            return dp[i]
        return dfs(0)