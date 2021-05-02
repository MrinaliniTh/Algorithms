# time complexit : O(n2)
# Space complexity : O(n)
# This algorithm is stable because order is maintained i.e, if there are duplicate value in array order will be same as before
# This algorithm is by default not adaptive, we can made it adaptive by adding a variable is_sorted, so that
# in best case if array is sorted, it compares n-1, so O(n) is best case
def bubble_sort(array, n):
    is_sorted = 0
    for i in range(n):
        is_sorted = 1
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = 0       
        if is_sorted:
            break
    return array


array = [7,12,65,6,23,9]
print(bubble_sort(array, len(array)))