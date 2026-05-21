class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Find the index of the target if it exists in nums."""

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1

        return -1