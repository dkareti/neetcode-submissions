class Solution:
    def climbStairs(self, n: int) -> int:
        """Find all possible ways with 1 or 2 steps to climb n steps."""
        if n == 1 or n == 2:
            return n

        prev2, prev1 = 1, 2

        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1