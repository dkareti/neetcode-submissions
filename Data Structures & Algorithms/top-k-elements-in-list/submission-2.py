class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Find the k top frequent numbers in an array."""
        count = {}

        for number in nums:
            count[number] = count.get(number, 0) + 1

        arr = list(count.items())
        sorted_arr = sorted(arr, key=lambda x:x[1], reverse=True)

        return [key for key, value in sorted_arr[:k]]