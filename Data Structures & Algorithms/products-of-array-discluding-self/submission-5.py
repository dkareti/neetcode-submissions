class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Find the product of an array except for an element."""
        result = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                result[i] = 1
            else:
                result[i] = result[i - 1] * nums[i - 1]

        postfix = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = 1
            else: 
                postfix[i] = nums[i + 1] * postfix[i + 1]

        for i in range(len(nums)):
            result[i] = result[i] * postfix[i]
        '''
        for example, where input = [1,2,4,6]
        - prefix = [1,1,2,8]
        - postfix = [48,24,6,1]
        result: prefix * postfix = [48, 24, 12, 8]
        '''

        return result