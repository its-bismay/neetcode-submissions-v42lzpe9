class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                currProfit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, currProfit)
            else:
                buy = sell
            
            sell += 1
        
        return maxProfit



        