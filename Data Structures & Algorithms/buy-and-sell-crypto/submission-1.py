class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Find the best price that can be obtained for a stock."""
        bought_stock_idx = 0
        max_profit = 0

        for sell_stock_idx, stock in enumerate(prices):
            if stock < prices[bought_stock_idx]:
                bought_stock_idx = sell_stock_idx

            max_profit = max(max_profit, stock - prices[bought_stock_idx])

        return max_profit


