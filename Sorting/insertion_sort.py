# time complexit : O(n2)
# Space complexity : O(n)
# This algorithm is stable because order is maintained i.e, if there are duplicate value in array order will be same as before
# This algorithm is by default adaptive
def insertion_sort(array, n):
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while(j >= 0 and array[j] > key):
            array[j + 1] = array[j]
            j -= 1
        array[j+1] = key
    return array


array = [7,12,65,6,23,9]
print(insertion_sort(array, len(array)))