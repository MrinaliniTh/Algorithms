#time complexity(nlog(n)), devide and conquer strategies which devides the problem into subproblems
# partitioning algorithm
# in best case its O(nlogn) but in worst case it O(n2)
def main(array):
    low = 0
    high = len(array) - 1
    return quicksort(array, low, high)

def quicksort(array, low, high):
    #find median as pivot
    i = low
    j = high
    med = low + (high - low)//2
    pivot = array[med]
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if low < j: 
        quicksort(array, low, j)
    if i < high: 
        quicksort(array, i, high)
    return array


array = [55, 17, 88, 7,12,65,6,23,9]
print(main(array))