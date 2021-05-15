#  O(n) time and O(1) space, usinf 3 pointers, left to track 0, right to track 2 and index for iteration
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = index = 0
        right = len(nums) - 1
        while index <= right:
            if nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            elif nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            else:
                index += 1
 # O(n) time and O(1) space, using add and subtract logic
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 1
        while i < len(nums):
            if nums[i] < nums[i - 1]:
                nums[i] = nums[i] + nums[i - 1]
                nums[i - 1] = nums[i] - nums[i - 1]
                nums[i] = nums[i] - nums[i - 1]
                i = 0
            i += 1