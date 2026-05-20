class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a dict
        storage = dict()

        for idx, value in enumerate(nums):
            #find the complement
            complement = target - value
            if complement in storage:
                return [storage[complement], idx]

            storage[value] = idx