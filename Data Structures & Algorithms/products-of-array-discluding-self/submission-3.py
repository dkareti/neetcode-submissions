class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Find the product of an array excluding the element itself."""
        result = [1] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                result[i] = 1
            else:
                result[i] = result[i - 1] * nums[i - 1]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i] 
        
        return result