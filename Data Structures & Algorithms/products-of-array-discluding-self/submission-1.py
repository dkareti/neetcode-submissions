class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Find the product of an array excluding the element itself."""
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        result = [1] * len(nums)
        def prod(nums: list[int]) -> int:
            ans = 1
            for item in nums:
                ans *= item
            return ans
        
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = 1
            else:
                postfix[i] = postfix[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i]
        return result