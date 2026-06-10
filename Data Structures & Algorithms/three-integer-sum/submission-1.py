class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Find all unique triplets that add to zero in nums."""
        result = []
        nums.sort()

        for i, value in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = value + nums[left] + nums[right]

                if total == 0:
                    result.append([value, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result