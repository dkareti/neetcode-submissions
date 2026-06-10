class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """Find the most consecutive ones."""
        max_length = 0
        curr_length = 0

        for item in nums:
            if item == 1:
                curr_length += 1
            if item == 0:
                curr_length = 0
            max_length = max(max_length, curr_length)

        return max_length