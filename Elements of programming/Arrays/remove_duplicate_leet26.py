# O(1) space and O(n) time
# shift duplicate values to the right and return right index, this approack doesnt delete the values
# instead if shifted to the right
class Solution:
    def removeDuplicates(self, nums) -> int:
        right_index = 1
        for i in range(1, len(nums)):
            if nums[right_index - 1] != nums[i]:
                nums[right_index] = nums[i]
                right_index += 1
        print(nums)
        return right_index


#  O(1) space and O(n) time, this approach deletes the values
class Solution:
    def removeDuplicates(self, nums) -> int:
        i=0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i+=1
        return len(nums)