class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        square_list = [ num * num for num in nums]
        print(square_list)
        i = 0
        j = len(nums) - 1
        while i <= j:
            if square_list[i] <= square_list[j]:
                res.append(square_list[j])
                j -= 1
            else:
                res.append(square_list[i])
                i += 1
        return res[::-1]