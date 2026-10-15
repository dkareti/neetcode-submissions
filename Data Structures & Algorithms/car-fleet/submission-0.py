class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """Find how many car fleets can be formed as cars travel on a one-lane highway."""
        pairs = [[pos, s] for pos, s in zip(position, speed)]
        sorted_arr = sorted(pairs, reverse=True)

        stack = []
        for pos, s in sorted_arr:
            time = (target - pos) / s
            stack.append(time)
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        
        return len(stack)