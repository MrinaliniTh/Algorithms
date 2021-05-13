# advantage:
# 1)stable algorithm
# 2)supoort large size list
# 3)can sort link list also
# 4)external sorting (loads only 1 element in RAM at the time)
# Disadvantage:
# 1)Extra space because of merge technique
# 2)No small problem: for less input it is inefficient
# Time: O(nlogn)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)

def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr = [3,2,5,8,7,5,6,0]
merge_sort(arr)
print(arr)