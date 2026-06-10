class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Find the superset of nums: all possible subsets of nums."""
        result = []

        def recurse(i, current):
            result.append(current[:])

            for j in range(i, len(nums)):
                current.append(nums[j])
                recurse(j + 1, current)
                current.pop()

        recurse(0, [])
        return result