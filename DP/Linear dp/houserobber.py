class Solution(object):
    def rob(self, nums):
        """
        Space-optimized DP for house robber problem.
        At each house, decide whether to rob or not based on adjacency constraint.
        
        Time: O(n), Space: O(1)
        Recurrence: max(current_house + rob1, rob2)
        rob1 = max money up to i-2, rob2 = max money up to i-1
        """
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2