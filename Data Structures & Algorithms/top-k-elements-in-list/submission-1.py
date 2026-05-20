from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = defaultdict(int)
        for item in nums:
            freq[item] += 1
        
        sortedList = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        sortedKeys = list(sortedList.keys())

        for i in range(0, k):
            ans.append(sortedKeys[i])

        return ans