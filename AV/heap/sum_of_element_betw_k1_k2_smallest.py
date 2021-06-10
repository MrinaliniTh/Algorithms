import heapq
def sum_of_element_betw_k1_and_k2_smallest_element(nums, k1, k2):
    p = find_k_smallest(nums, k1)
    q = find_k_smallest(nums, k2)
    print(p,q)
    sum = 0
    for num in nums:
        if num > p and num < q:
            sum += num
    return sum

def find_k_smallest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    res = []
    while k > 0:
        res.append(heapq.heappop(heap))
        k -= 1
    return res[-1]

print(sum_of_element_betw_k1_and_k2_smallest_element([1,3,12,5,15,11], 2, 4))