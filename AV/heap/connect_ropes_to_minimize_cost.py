import heapq
def connect_ropes_to_mininize_cost(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    cost = 0
    while len(heap) >= 2:
        rope1 = heapq.heappop(heap)
        rope2 = heapq.heappop(heap)
        cost = cost + rope1 + rope2
        heapq.heappush(heap, rope1+ rope2)
    return cost

print(connect_ropes_to_mininize_cost([1,2,3,4,5]))