class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Find the two values in the array that add up to the target"""
        seen = {}

        for idx, value in enumerate(nums):
            complement = target - value

            if complement in seen:
                return [seen[complement], idx]

            seen[value] = idx