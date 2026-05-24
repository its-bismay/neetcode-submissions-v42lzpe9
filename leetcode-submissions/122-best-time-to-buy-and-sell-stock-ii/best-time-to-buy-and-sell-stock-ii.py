class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        totalProfit = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
                sell += 1
            else:
                currProfit = prices[sell] - prices[buy]
                totalProfit = currProfit + totalProfit
                buy = sell
                sell += 1
        
        return totalProfit
                

        