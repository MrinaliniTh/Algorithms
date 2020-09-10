# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

def contains_duplicate(nums:list)->bool:
    temp_dict = {}
    for num in nums:
        if num in temp_dict:
            return True
        else:
            temp_dict[num] = 1
    return False

print(contains_duplicate([1,2,3,4]))