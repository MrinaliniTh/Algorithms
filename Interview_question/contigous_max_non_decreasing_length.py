# Your array is not sorted, you need to find the maximum length of non decreasing order
def contigous_max_non_decreasing_length(arr):
    left = right = 0
    max_length = float("-inf")
    while right < len(arr) - 1:
        if arr[right] < arr[right + 1]:
            right += 1
        else:
            max_length = max(max_length, right - left + 1)
            right += 1
            left = right
    return max_length


arr = [1,2,3,4,2,5,6,7,10,16,1,8,9]
print(contigous_max_non_decreasing_length(arr))