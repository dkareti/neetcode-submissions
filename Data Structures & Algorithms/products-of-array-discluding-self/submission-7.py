class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Find the product of an array except for an element."""
        result = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        '''
        for example, where input = [1,2,4,6]
        - prefix = [1,1,2,8]
        - postfix = [48,24,6,1]
        result: prefix * postfix = [48, 24, 12, 8]
        '''

        return result