class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)
        buy = 0

        for sell in range(1, n):
            if prices[sell] < prices[buy]:
                buy = sell
                sell += 1
            else:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])

        return maxProfit

        