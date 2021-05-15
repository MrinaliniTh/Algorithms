# find maximu contigous subarray which sums to target sum
def max_contiguous_subarray_sum(arr, sum):
    temp_list = []
    max_len = float("-inf")
    left = right = 0
    cur_sum = 0
    while right < len(arr):
        cur_sum += arr[right]
        if cur_sum == sum:
            max_len = max(max_len, right-left+1)
            cur_sum -= arr[right]
            left += 1
            right += 1
        if cur_sum > sum:
            while cur_sum > sum:
                cur_sum -= arr[left]
                left += 1
            if cur_sum == sum:
                max_len = max(max_len, right-left+1)
                left += 1
            right += 1
        else:
            right += 1
    return max_len


arr = [2,5,3,10,6]
sum = 6
print(max_contiguous_subarray_sum(arr, sum))
# Above soulution cannot handle negative case, for that check leetcode560.py