import heapq
def frequencySort(self, nums):
    temp = {}
    for num in nums:
        if num in temp:
            temp[num] += 1
        else:
            temp[num] = 1
    heap = []
    for key, val in temp.items():
        heapq.heappush(heap, (val, key))
    res = []
    print(heap)
    while heap:
        pop_item = heapq.heappop(heap)
        freq = pop_item[0]
        num = pop_item[1]
        while freq:
            res.append(num)
            freq -= 1
    return res