import heapq
def find_k_closest(nums, k, x):
    heap = []
    for num in nums:
        diff = abs(x - num)
        heapq.heappush(heap, (diff, num))
    res = []
    while k > 0:
        res.append(heapq.heappop(heap)[1])
        k -= 1
    return sorted(res)

print(find_k_closest([1,2,3,4,5], 2, 5))