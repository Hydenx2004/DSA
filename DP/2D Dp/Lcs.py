class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        2D DP for finding LCS between two strings.
        Compare characters and either match or take max of skipping one character.
        
        Time: O(m*n), Space: O(m*n)
        dp[i][j] = LCS length for text1[i:] and text2[j:]
        Recurrence: if match: 1 + dp[i+1][j+1], else: max(dp[i+1][j], dp[i][j+1])
        """
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]