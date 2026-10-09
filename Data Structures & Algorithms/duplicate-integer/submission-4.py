class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """Determine if an array has a duplicate."""
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        
        return False