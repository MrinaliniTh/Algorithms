import copy

def combination_sum(num):
    candidates = [i + 1 for i in range(num)]
    combinations = []
    res = []
    find_combination(res, combinations, candidates, num, 0)
    return res

def find_combination(res, combinations, candidates, target, start):
    if target == 0:
        res.append(copy.deepcopy(combinations))
        return
    for i in range(start, len(candidates)):
        if candidates[i] > target:
            break
        combinations.append(candidates[i])
        find_combination(res, combinations, candidates, target - candidates[i], i)
        combinations.pop()

print(combination_sum(3))