class Solution:
    def maxProfit(self, prices) -> int:
        sum = 0
        for i in range(len(prices)-1):
            if prices[i + 1] > prices[i]:
                sum += prices[i + 1] - prices[i]
        return sum
