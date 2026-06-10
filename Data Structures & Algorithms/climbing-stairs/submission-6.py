class Solution:
    def climbStairs(self, n: int) -> int:
        """Find the ways to climb n stair using only one or two steps."""
        if n <= 2:
            return n

        one_step_back = 2
        two_steps_back = 1

        for _ in range(3, n + 1):
            current_sum = one_step_back + two_steps_back
            two_steps_back = one_step_back
            one_step_back = current_sum

        return current_sum