import heapq
def topKFrequent(nums, k):
    temp = {}
    for num in nums:
        if num in temp:
            temp[num] += 1
        else:
            temp[num] = 1
    heap = []
    for key, val in temp.items():
        heapq.heappush(heap, (val, key))
        if len(heap) > k:
            heapq.heappop(heap)
    res = []
    for num in heap:
        res.append(num[1])
    return res

print(topKFrequent([1,1,1,2,2,3], 2))