import copy
class Solution:
    def combinationSum(self, candidates, target: int):
        res = []
        if not candidates:
            return res
        combinations = []
        candidates = sorted(candidates)
        self.find_combination(res, combinations, candidates, target, 0)
        return res

    def find_combination(self, res, combinations, candidates, target, start):
        if target == 0:
            res.append(copy.deepcopy(combinations))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            combinations.append(candidates[i])
            self.find_combination(res, combinations, candidates, target - candidates[i], i)
            combinations.pop()