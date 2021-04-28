def find_fibonacci_series(num):
    dp = [0] * num
    dp[0] = 0
    dp[1] = 1
    for i in range(2, num):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[num-1]


def fib_with_memoization(num):
    dp = [0 for _ in range(num)]
    res = find_fib(num-1, dp)
    return dp

def find_fib(num, dp):
    if num <=1:
        return num
    if dp[num] != 0:
        return dp[num]
    dp[num] = find_fib(num-1, dp) + find_fib(num-2, dp)
    return dp[num]
print(fib_with_memoization(6))