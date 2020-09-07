# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def two_sum_array(nums:list, target:int) -> list:
    temp_dict = {}
    for i, num in enumerate(nums):
        final_target = target - num
        if final_target in temp_dict:
            return [temp_dict[final_target], i]
        else:
            temp_dict[num] = i


print(two_sum_array([2,7,11,15], 9))