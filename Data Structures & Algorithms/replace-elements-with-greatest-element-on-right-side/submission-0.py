class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """Replace the elements with the greatest subsequent element."""
        for i in range(len(arr) - 1):
            subarr = arr[i+1:]
            arr[i] = max(subarr)

        arr[-1] = -1
        return arr