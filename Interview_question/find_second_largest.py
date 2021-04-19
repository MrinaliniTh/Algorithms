def find_second_largest(nums):
    largest = 0
    second_largest = 0
    for num in nums:
        if num > largest:
            largest = num
            second_larget = largest
        elif num > second_largest:
            second_largest = num
    return second_largest, largest

print(find_second_largest([3,5,18,5,20,7,1]))