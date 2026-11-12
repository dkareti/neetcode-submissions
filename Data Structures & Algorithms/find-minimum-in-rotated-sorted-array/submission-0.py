class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Find the smallest value in a rotated sorted array."""
        smallest = float('inf')
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            smallest = min(nums[mid], smallest)
            if nums[mid] < nums[high]:
                high = mid - 1
            else:
                low = mid + 1
        return smallest