import heapq
def kth_smallest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    res = []
    while k > 0:
        res.append(heapq.heappop(heap))
        k -= 1
    print(res)
    return res[-1]

print(kth_smallest([10, 3, 5, 1, 9], 2))
