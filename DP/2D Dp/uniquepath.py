class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Space-optimized 2D DP for counting unique paths in grid.
        Can only move right or down, so paths[i][j] = paths[i+1][j] + paths[i][j+1]
        
        Time: O(m*n), Space: O(n)
        Working backwards from bottom-right to top-left
        """
        row = [1] * n
        for i in range(m-1):
            newrow = [1] * n
            for j in range(n-2, -1, -1):
                newrow[j] = newrow[j+1] + row[j]
            row = newrow
        return row[0]