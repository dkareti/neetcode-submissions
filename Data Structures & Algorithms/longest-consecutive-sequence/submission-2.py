class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Find the longest consecutive sequence."""
        longest = 0
        candidates = set(nums)
        
        for value in nums:
            if (value - 1) not in candidates: #value is the start of a sequence
                length = 0
                while value + length in candidates:
                    length += 1
                longest = max(length, longest)
        
        return longest
