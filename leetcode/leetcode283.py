def swap_zero_to_left2(nums):
    left = 0 
    right = 0
    while left < len(nums):
        if nums[left] != 0:
            nums[right],nums[left] = nums[left], nums[right]
            right += 1
        left += 1
    return nums