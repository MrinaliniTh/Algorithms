def largest_subarray_sum(array):
    max_so_far = float("-inf")
    max_ending = 0
    start = end = beg = 0
    for i, num in enumerate(array):
        max_ending += num
        if max_ending < 0:
            max_ending = 0
            beg += 1
        if max_so_far < max_ending:
            max_so_far = max_ending
            start = beg
            end = i
        
    print(array[start: end + 1])
    return max_so_far

print(largest_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]))
        