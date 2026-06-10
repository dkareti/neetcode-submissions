class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Find unique subsets of nums."""
        nums.sort()
        result = []

        def recurse(i, current):
            if current[:] not in result:
                result.append(current[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                current.append(nums[j])
                recurse(j + 1, current)
                current.pop()

        recurse(0, [])
        return result