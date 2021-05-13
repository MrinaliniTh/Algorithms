# Find max contiguous subarray sum for size k
def max_sum_subarray_sum_size_k(arr, k):
    sum = 0
    max_sum = float("-inf")
    left = right = 0
    while right < len(arr):
        sum += arr[right]
        if right - left + 1 == k:
            max_sum = max(max_sum, sum)
            sum -= arr[left]
            left += 1
            right += 1
        else:
            right += 1
    return max_sum

arr = [2,5,3,10,6]
k = 2
print(max_sum_subarray_sum_size_k(arr, k))