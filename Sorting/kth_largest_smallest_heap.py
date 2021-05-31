import heapq
# If kth largest then use min heap
def kth_largest(nums, k):
    res = []
    for num in nums:
        heapq.heappush(res, num)
        print(res)
        if len(res) > k:
            heapq.heappop(res)
    return res[0]

# If kth smallest then use max heap
def kth_smallest(nums, k):
    res = []
    for num in nums:
        res.append(num)
        
        if len(res) > k:
            sorted(res)
            res.reverse()
            print(res)
            res.pop()
    print(res)
    return res[-1]
print(kth_smallest([3,2,1,5,6,4], 3))