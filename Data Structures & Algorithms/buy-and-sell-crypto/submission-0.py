class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Find the max profit that can be earned."""
        left = 0
        max_sum = 0

        for right, stock in enumerate(prices):
            if stock >= prices[left]:
                max_sum = max(max_sum, stock - prices[left])
            else:
                left = right

        return max_sum
