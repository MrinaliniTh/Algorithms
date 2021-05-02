# find maximum profit from knapsack
# Using recursion or top down approach
def find_max_profit_from_knapsack(weight, val, capacity, size):
    if (size == 0 or capacity == 0):
        return 0
    if weight[size-1] <= capacity:
        return max(val[size-1] + find_max_profit_from_knapsack(weight, val, capacity - weight[size-1], size-1),
        find_max_profit_from_knapsack(weight, val, capacity, size-1))
    else:
        return find_max_profit_from_knapsack(weight, val, capacity, size-1)

#Using recursion with memoization
def find_max_profit_from_knapsack_memoize(weight, val, capacity, size):
    dp = [ [0 for j in range(capacity+1)] for i in range(size+1)]
    find_max_profit(weight, val, capacity, size, dp)
    return dp[size][capacity]

def find_max_profit(weight, val, capacity, size, dp):
    if size == 0 or capacity == 0:
        return 0
    if dp[size][capacity] != 0:
        return dp[size][capacity]
        
    if weight[size-1] <= capacity:
        dp[size][capacity] = max(val[size-1] + find_max_profit(weight, val, capacity-weight[size-1], size-1, dp),
                                find_max_profit(weight, val, capacity, size-1, dp))
        return dp[size][capacity]
    else:
        dp[size][capacity] = find_max_profit(weight, val, capacity, size-1, dp)
        return dp[size][capacity]

# Using dp or bottom up approach
def find_max_profit_from_knapsack_dp(weight, val, capacity, size):
    dp = []
    dp = [ [0 if j == 0 or i == 0 else -1 for j in range(capacity+1)] for i in range(size+1)]
    for i in range(1, size+1):
        for j in range(1, capacity + 1):
            if weight[i-1] <= j:
                dp[i][j] = max(val[i-1] + dp[i-1][j - weight[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[size][capacity]



wt = [1,4,1,3,2]
val=[20,10,5,20,8]
size = 9
print(find_max_profit_from_knapsack_dp(wt, val, size, len(wt)))