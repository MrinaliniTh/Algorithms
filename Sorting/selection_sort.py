# time complexit : O(n2)
# Space complexity : O(n)
# This algorithm is not stable because order is not maintained i.e, if there are duplicate value in array order will not be same as before
# This algorithm is not adaptive beacuse it again traverse the arrays and compares n number of times
def selection_sort(array, n):
    for i in range(n-1):
        min = i
        j = i + 1
        while j < n:
            if array[j] < array[min]:
                min = j
            j += 1
        if i != min:
            array[i], array[min] = array[min], array[i]
    return array


array = [12,1,65,6,23,10,0,9]
# array = [1,12,9,0,5,35]
print(selection_sort(array, len(array)))