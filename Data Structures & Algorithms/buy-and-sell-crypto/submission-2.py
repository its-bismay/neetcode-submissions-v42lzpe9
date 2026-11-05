class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        for idx, value in enumerate(prices):
            profit = value - buy
            maxProfit = max(maxProfit, profit)
            if value < buy:
                buy = value
        
        return maxProfit
            
        