import heapq

def find_second_largest(nums):
    largest = 0
    second_largest = 0
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest, largest

def find_using_heapq(nums, k):
    val = nums[0:k]
    heapq.heapify(val)
 
    for i in range(k, len(nums)):
        if nums[i] > val[0]:
            heapq.heapreplace(val, nums[i])

    return val[0]

# print(find_second_largest([3,5,18,25,20,7,1]))
print(find_using_heapq([3,5,18,25,20,7,1], 2))