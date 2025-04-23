# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            middle = (left + right) // 2
            g = guess(middle)
            if g == -1:
                right = middle - 1
            elif g == 1:
                left = middle + 1
            else:
                return middle

        if guess(left):
            return left
        if guess(right):
            return right
        return -1
        
