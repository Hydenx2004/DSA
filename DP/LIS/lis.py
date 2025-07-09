class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Bottom-up DP working backwards to find LIS length.
        For each position, look at all future elements and extend if possible.
        
        Time: O(n²), Space: O(n)
        dp[i] = length of LIS starting at index i
        Recurrence: dp[i] = max(dp[i], 1 + dp[j]) where nums[i] < nums[j]
        """
        dp = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)