# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one. Meanwhile,
# adjacent houses have a security system connected, and it will automatically contact the police if two 
# adjacent houses were broken into on the same night.

# Given a list of non-negative integers nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.
# space complexity: O(n)
# time complexity: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 3: return max(nums)

        def find_max(dp):
            dp[1] = max(dp[0], dp[1])
            for i in range(2, len(dp)):
                dp[i] = max(dp[i] + dp[i-2], dp[i-1])
            return dp[-1]
        return max(find_max(nums[:len(nums)-1]), find_max(nums[1:]))