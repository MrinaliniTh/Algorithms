def max_sum_subarray_sizeK(array, k):
    max_sum = float("-inf")
    left = right = 0
    sum = 0
    while right < len(array):
        sum += array[right]
        if right - left + 1 == k:
            max_sum = max(max_sum, sum)
            sum -= array[left]
            left += 1
        
        right += 1
    return max_sum


print(max_sum_subarray_sizeK([2,5,1,8,2,9,1], 4))