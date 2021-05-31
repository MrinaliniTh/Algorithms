def is_connected(nums):
    items = [i for i in range(len(nums))]
    num_circle = len(items)
    print(items)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i][j] == 1:
                    num_circle = mark_union(nums, items, i, j, num_circle)
    return num_circle

def mark_union(nums, items, row, col, num_circle):
    freind_circle = num_circle
    repr_A = find(items, row)
    repr_B = find(items, col)
    if repr_A != repr_B:
        items[col] = repr_A
        freind_circle -= 1
    return freind_circle

def find(items, person):
    if items[person] == person:
        return person
    find(items, items[person])
print(is_connected([[1,0,0],[0,1,0],[0,0,1]]))