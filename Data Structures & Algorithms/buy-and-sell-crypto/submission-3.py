class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        "Find the max profit that you can gain"
        left = 0
        max_profit = 0
        
        for right, price in enumerate(prices):          
            if price < prices[left]:
                left = right

            max_profit = max(max_profit, price - prices[left])
            
        return max_profit
