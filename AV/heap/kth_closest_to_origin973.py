# For this, we need nearest value, so we will be using heap
import heapq
def kth_closest_to_origin(points, k):
    heap = []
    for x, y in points:
        dist = x * x + y * y # √(x1 - x2)2 + (y1 - y2)2). here origin is 0,
        # so x1 = 0 and y1= 0 so not including, here we are not calculating squaroot to save computation time.
        heapq.heappush(heap, [dist, (x, y)])
    res = []
    while k > 0:
        res.append(heapq.heappop(heap)[1])
        k -= 1
    return res

print(kth_closest_to_origin([[1,3],[-2,2]], 1))
print(kth_closest_to_origin([[3,3],[5,-1],[-2,4]], 2))
