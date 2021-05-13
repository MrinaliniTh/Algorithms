# using while loop
def binary_search(nums, key):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if key == nums[mid]:
            return mid + 1
        elif key < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# using recursion(O(log(n)), in best case it is O(1))
def binary_search_recursion(nums, key):
    return bs(nums, 0, len(nums) - 1, key)

def bs(nums, left, right, key):
    if left <= right:
        mid = (left + right) // 2
        if key == nums[mid]:
            return mid + 1
        elif key < nums[mid]:
            return bs(nums, left, mid - 1, key)
        else:
            return bs(nums, mid + 1, right, key)

nums = [3,4,5,7,1,9]
nums = sorted(nums)
print(nums)
print(binary_search_recursion(nums, 9))