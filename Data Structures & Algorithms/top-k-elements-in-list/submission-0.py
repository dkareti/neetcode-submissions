from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        occur = defaultdict(int)
        nums.sort()
        for i in range(0, len(nums)):
            value = nums[i]
            if(occur[value] == k-1):
                ans.append(value)
            occur[value] += 1
        return ans