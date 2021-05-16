class Solution:
    def maxProfit(self, prices) -> int:
        buy_stock = float("inf")
        sale_stock = 0
        for price in prices:
            if price < buy_stock:
                buy_stock = price
            else:
                sale_stock = max(sale_stock, price - buy_stock)
        return sale_stock

# Input: prices = [7,1,5,3,6,4]
# Output: 5 (buy on day 2(1) and sell it on day 5(6) ==> 6 - 1 = 5)