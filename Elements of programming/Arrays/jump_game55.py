class Solution:
    def canJump(self, nums) -> bool:
        max_reach_so_far = 0
        dest = len(nums) - 1
        i = 0
        while i <= max_reach_so_far and max_reach_so_far < dest:
            max_reach_so_far = max(max_reach_so_far, nums[i] + i)
            i += 1
        return max_reach_so_far >= dest