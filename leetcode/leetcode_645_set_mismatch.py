def findErrorNums(nums):
    i = 1
    while i in nums:
        i += 1
    nums = sorted(nums)
    for j in range(len(nums) - 1):
        if nums[j] == nums[j + 1]:
            return [nums[j], i]
print(findErrorNums([1,2,2]))

def findErrorNums2(nums):
    set_data = set()
    dup = 0
    for i in nums:
        if i in set_data:
            dup = i
        else:
            set_data.add(i)
    total_sum = sum(set_data)
    sum_data = int((len(nums) * (len(nums) + 1)) / 2) # ap(formula) = n(n+1)/2 where n is lenght of nums, this will give the total sum
    return [dup, sum_data-total_sum]
print(findErrorNums2([1,2,2]))
                
            
        