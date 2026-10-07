class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Find two numbers that add to the target."""
        seen = collections.defaultdict(int)

        for idx, value in enumerate(numbers):
            complement = target - value
            if complement in seen:
                return [seen[complement], idx + 1]
            seen[value] = idx + 1

            