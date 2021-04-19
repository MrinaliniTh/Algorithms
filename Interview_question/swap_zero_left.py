# approach 1
def swap_zero_to_left(nums):
    temp_list = []
    for i, num in enumerate(nums):
        if num == 0:
            nums.remove(nums[i])
            temp_list.append(num)
    return nums + temp_list
# approach 2
def swap_zero_to_left2(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1
    return nums
print(swap_zero_to_left2([1,4,0,5,7,0,2,4,5]))
