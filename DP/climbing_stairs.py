# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# space complexity= O(n), time complexity= O(n)

def climbing_stairs(n:int)->int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        cur = dp[i-1] + dp[i-2]
        dp[i] = cur
    return dp[-1]

res = climbing_stairs(4)
print(res)
    