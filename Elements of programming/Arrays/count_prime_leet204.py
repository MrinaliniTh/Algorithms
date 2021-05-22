class Solution:
    def countPrimes(self, n: int) -> int:
        nums = []
        prime_count = 0
        for i in range(n):
            nums.append(True)
        i = 2
        while i * i < n:
            j = i
            while j * i < n:
                nums[j * i] = False
                j += 1
            i += 1
        i = 2
        while i < n:
            if nums[i]:
                prime_count += 1
            i += 1
        return prime_count

# first assign all list with True
# iterate from index i = 2, and for the index i check all multiples and mark with False
# now count from index i = 2 and check if its True
        