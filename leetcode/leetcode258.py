# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            question = num // 10
            remainder = num % 10
            num = question + remainder
        return num 

# Input: num = 38
# Output: 2