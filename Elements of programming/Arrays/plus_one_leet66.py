# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

def plus_one(nums):
    for i in reversed(range(len(nums))):
        if nums[i] < 9:
            nums[i] += 1
            return nums
        else:
            nums[i] = 0
    nums[0] = 1
    nums.append(0)
    return nums

print(plus_one([1, 8, 9]))
