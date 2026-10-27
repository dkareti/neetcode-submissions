class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Find the smallest value k that Koko must eat per hour to finish all the bananas."""
        if h == len(piles):
            return max(piles)
        low = 1
        high = max(piles)
        lowest = float('inf')

        def checkValidity(candidate: int) -> int:
            remaining_hours = h
            for i in range(len(piles)):
                remaining_hours -= math.ceil(piles[i] / candidate)
            if remaining_hours >= 0:
                return True
            else:
                return False
        
        while low <= high:
            k = (low + high) // 2
            if checkValidity(k):
                lowest = min(k, lowest)
                high = k - 1
            else:
                low = k + 1
        
        return lowest
            
        
                