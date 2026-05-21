class Solution:
    def climbStairs(self, n: int) -> int:
        """Find all possible ways with 1 or 2 steps to climb n steps."""
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)