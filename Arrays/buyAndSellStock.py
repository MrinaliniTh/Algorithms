# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Iterative approach(O(n) space, O(n) time complexity)
# maintain two variable initially i.e, sale_stock and buy_stock
# Iterate over prices
# buy_stock will be assigned as infinity at the begining
# sale_stock will be 0 at the begining
# if price is less than buy stock, replace buy stock with the price
# else replace sale_stock with max of (sale_stock, price - buy_stock)
# return sale_stock

def buy_and_sell_stock(prices:list)->int:
    sale_stock = 0
    buy_stock = float("inf")
    for price in prices:
        if price < buy_stock:
            buy_stock = price
        else:
            sale_stock = max(sale_stock, price - buy_stock)
    return sale_stock

print(buy_and_sell_stock([7,3,5,1,6,4]))