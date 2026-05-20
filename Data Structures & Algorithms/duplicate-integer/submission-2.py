class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create dict
        storage = dict()

        for value in nums:
            #check if it already exists
            if value in storage:
                return True

            storage[value] = 1

        return False