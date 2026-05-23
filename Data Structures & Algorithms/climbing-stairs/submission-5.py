class Solution:
    def climbStairs(self, n: int) -> int:
        """Count the number of ways a person can climb n stairs if they either take 2 steps at a time or 1 step."""
        if n <= 2:
            return n

        climbing_one_step_back = 2 # n = 2
        climbing_two_steps_back = 1 # n = 1

        for _ in range(3, n+1):
            current = climbing_one_step_back + climbing_two_steps_back
            climbing_two_steps_back = climbing_one_step_back
            climbing_one_step_back = current

        return current