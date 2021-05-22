
def permute(nums):
    permutations = []
    get_permutations(nums, [], permutations)
    return permutations

def get_permutations(array, cur, permutations):
    if not array and cur:
        permutations.append(cur)
    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i + 1: ]
            new_permutations = cur + [array[i]]
            get_permutations(new_array, new_permutations, permutations)

# print(permute([1,2,3]))
print(permute(["a", "b", "c"]))