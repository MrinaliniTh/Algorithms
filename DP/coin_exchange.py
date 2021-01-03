# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.
# space complexity: O(n)
# time complexity: O(n2)

# You may assume that you have an infinite number of each kind of coin.
amount = 3
coins = [2]

def coin_exchange(amount:int, coins:list)-> int:
    if len(coins) == 0 or amount == 0:
        return 0
    dp = [amount + 1] * (amount+1)
    dp[0] = 0
    for i in range(amount + 1):
        for j in coins:
            if i >= j:
                dp[i] = min(dp[i-j] + 1, dp[i])
    return dp[-1] if dp[-1] != amount + 1 else -1
    
res = coin_exchange(amount, coins)
print(res)
