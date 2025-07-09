class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Greedy approach working backwards from end.
        Update goal position whenever we can reach current goal.
        
        Time: O(n), Space: O(1)
        If we can reach current goal from position i, update goal to i
        """
        goal = len(nums) - 1
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0