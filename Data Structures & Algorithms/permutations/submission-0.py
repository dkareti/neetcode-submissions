class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Find the possible permutations for nums."""
        result = []

        def recurse(i):
            if i == len(nums):
                result.append(nums[:])
                return
            
            for j in range(i, len(nums)):
                nums[j], nums[i] = nums[i], nums[j]
                recurse(i + 1)
                nums[j], nums[i] = nums[i], nums[j]

        recurse(0)
        return result