# find first occurance on 1's in sorted 0's and 1's in an array
# i/p::[0,0,0,0,1,1,1,1]
# o/p :: 4
 
def find_first_one(nums):
    low = 0
    high = len(nums) - 1
    if nums[0] == 1:
        return 0
    while low <= high:
        mid = int((low + high) / 2)
        if nums[mid] == 1 and nums[mid - 1] == 0:
            return mid
        elif nums[mid] == 1:
            high = mid -1
        else:
            low = mid + 1
    return -1

print(find_first_one([0,0,0,0,0,1,1,1,1,1,1,1]))
