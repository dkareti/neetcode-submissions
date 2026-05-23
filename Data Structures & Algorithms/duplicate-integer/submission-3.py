class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """Find if an array has duplicate values."""
        seen = set()

        for value in nums:
            if value in seen:
                return True
            seen.add(value)

        return False