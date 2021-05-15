class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        temp_dict = {0 : 1}
        sum = 0
        count = 0
        for i in range(len(arr)):
            sum += arr[i]
            if sum - k in temp_dict:
                count += temp_dict[sum - k]
            temp_dict[sum] = temp_dict.get(sum, 0) + 1
        return count