# Given an integer array nums, 
# find the contiguous subarray within an array (containing at least one number) which has the largest product.
# take a product from left side and stor the max result and then take a prouct from right side and take the max result
def max_prod_subarray(nums:list) -> int:
    prod = 1
    res = float("-inf")
    for num in nums:
        prod = prod * num
        res = max(res, prod)
        if prod == 0:
            prod = 1
    prod = 1
    for num in nums[::-1]:
        prod = prod * num
        res = max(res, prod)
        if prod == 0:
            prod = 1
    return res
print(max_prod_subarray([-2,0,-1]))