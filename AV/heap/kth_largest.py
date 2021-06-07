import heapq
def kth_largest_value(array, k):
    heap = []
    for num in array:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    print(heap)
    return heap[0]

print(kth_largest_value([10, 2, 5, 3, 9], 2))