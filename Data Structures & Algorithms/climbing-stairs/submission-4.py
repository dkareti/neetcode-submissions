class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        climb_two_steps = 1
        climb_one_step = 2

        for _ in range(3, n + 1):
            current = climb_one_step + climb_two_steps
            climb_two_steps = climb_one_step
            climb_one_step = current

        return current