# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        above, below = n + 1, 0
        res = guess(n // 2)
        foo = n // 2
        while res != 0:
            if res < 0:
                above = foo
            else:
                below = foo
                
            foo = (above + below) // 2
                
            res = guess(foo)
        
        return foo
            
        
