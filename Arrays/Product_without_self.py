# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements
# of nums except nums[i].


# Iterative approach: Space O(n), Time O(n)
# Take a product from left side
# Take a product from right side
# multiply with the left and right product
# Example:
# left_product = [1,1,1,1] , right_product = [1,1,1,1] initially
# after multiplying from left side left_product = [1,1,2,6]
# after multiplying from right side right_product = [24,12,4,1]
# return product from both list
def productExceptSelf(nums: list) -> list:
    left_product = [1] * len(nums)
    right_product = [1] * len(nums)
    i = 1
    while i < len(nums):
        left_product[i] = left_product[i-1] * nums[i-1]
        i += 1
    j = len(nums) - 2
    while j >= 0:
        right_product[j] = right_product[j+1] * nums[j+1]
        j -= 1
    return [left_product[i] * right_product[i] for i in range(len(nums))]

print(productExceptSelf([1,2,3,4]))

