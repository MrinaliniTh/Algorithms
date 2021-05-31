class Solution:
    def rotate(self, nums) -> None:
        """
        rotate array except mif element, if even then
        there will be two mid element else there will be one
        """
        k = len(nums) // 2
        if len(nums) % 2 != 0:
            self.reverse(nums, 0, len(nums) - 1)
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k + 1, len(nums) - 1)
            return nums
        else:
            self.reverse(nums, 0, len(nums) - 1)
            self.reverse(nums, 0, k - 2)
            self.reverse(nums, k + 1, len(nums) - 1)
            self.reverse(nums, k - 1, k)
            return nums

    def reverse(self, nums, low, high):
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1

obj = Solution()
# print(obj.rotate([1,2,3,4,5,6,7])) # output: [5,6,7,4,1,2,3] // for odd lenght
# print(obj.rotate([1,2,3,4,5,6,7,8])) # output: [6,7,8,4,5,1,2,3] // for even lenght
# print(obj.rotate([1,2,3,4,5,6,7,8,9,10])) # [7, 8, 9, 10, 5, 6, 1, 2, 3, 4] // for even lenght
print(obj.rotate([1,2,3,4,5,6,7,8,9,10,11,12]))