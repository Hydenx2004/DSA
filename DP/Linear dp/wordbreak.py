class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Bottom-up DP working backwards from end of string.
        Check if substring starting at i can be broken using wordDict.
        
        Time: O(n * m * k), Space: O(n)
        n = len(s), m = len(wordDict), k = avg word length
        dp[i] = True if s[i:] can be broken into words
        """
        word_dict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s)-1, -1, -1):
            for word in word_dict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]