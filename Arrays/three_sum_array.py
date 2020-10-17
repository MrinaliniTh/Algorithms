# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
# Solution::
# three pointer approach, space= o(n), time= o(n2)
# take two pointer left and right
# if res(current+left+right) is 0 increase left and decrease right
# else if res < 0 increase left
# else decrease right
# handle duplicates:
# handle at the begining:: check if index i not equal to 0 and nums[i] == nums[i-1], because if it is equal then we will check the same process again which 
# will tend to result in duplicate array
# handle in between :: when we get res = 0 check if left element is equal to left + 1 element, if it does then increase left(because we dont want to compute again)
# same for right, check if right element is equal to right-1, then decrease right

def three_sum_array(nums:list) -> list:
    if len(nums) <= 2:
        return []
    main_list = []
    nums = sorted(nums)
    for i in range(0,len(nums)-2):
        if i != 0 and nums[i] == nums[i-1]: continue
        left = i+1
        right = len(nums)-1
        while left < right:
            res = nums[i] + nums[left] + nums[right]
            if res == 0:
                main_list.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif res < 0:
                left += 1
            else:
                right -= 1
    return main_list



print(three_sum_array([-2,0,0,2,2]))