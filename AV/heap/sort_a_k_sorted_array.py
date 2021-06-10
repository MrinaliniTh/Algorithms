import heapq
def sort_k_sorted_array(array, k):
    heap = []
    res = []
    for num in array:
        heapq.heappush(heap, num)
        if len(heap) > k:
            res.append(heapq.heappop(heap))
    while len(heap):
        res.append(heapq.heappop(heap))
    return res


print(sort_k_sorted_array([2, 6, 3, 12, 56, 8], 3))