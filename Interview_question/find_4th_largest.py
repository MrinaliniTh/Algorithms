def find_fourth_largest(nums):
    i = 1
    n = len(nums)
    while i < n:
        if nums[i-1] < nums[i]:
            nums[i] = nums[i] + nums[i-1]
            nums[i-1] = nums[i] - nums[i-1]
            nums[i] = nums[i] - nums[i-1]
            i = 0
        i += 1
    return nums[3]
print(find_fourth_largest([1,3,2,4,6,5]))
