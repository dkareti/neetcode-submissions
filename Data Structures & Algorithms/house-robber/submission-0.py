class Solution:
    def rob(self, nums: List[int]) -> int:
        """Find the max sum from non-adjacent houses"""
        if len(nums) <= 2:
            return max(nums)

        prev2 = nums[0]
        prev1 = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            current = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = current

        return current