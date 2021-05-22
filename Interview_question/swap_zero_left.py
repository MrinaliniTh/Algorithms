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
    left = 0 
    right = 0
    while left < len(nums):
        if nums[left] != 0:
            nums[right],nums[left] = nums[left], nums[right]
            right += 1
        left += 1
    return nums
print(swap_zero_to_left2([1,3,5,0,4,0,6,0]))
