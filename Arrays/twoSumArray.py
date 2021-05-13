# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Hash table complement method on unsorted list with O(n)
def two_sum_array(nums:list, target:int) -> list:
    temp_dict = {}
    for i, num in enumerate(nums):
        final_target = target - num
        if final_target in temp_dict:
            return [temp_dict[final_target], i]
        else:
            temp_dict[num] = i

# Two pointer method on sorted list with O(nlogn)
def two_sum_array_using_two_pointer(nums, target):
    res = []
    nums = sorted(nums)
    for i in range(0, len(nums) - 2):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        low = i
        high = len(nums)-1
        while low < high:
            sum_ = nums[low] + nums[high]
            if sum_ == target:
                if [nums[low], nums[high]] not in res:
                    res.append([nums[low], nums[high]])
                while low < high and nums[low] == nums[low+1]:
                    low += 1
                while low < high and nums[high] == nums[high-1]:
                    high -= 1
                low += 1
                high -= 1
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1
    return res

print(two_sum_array_using_two_pointer([-1,0,1,2,1,-4], -3))