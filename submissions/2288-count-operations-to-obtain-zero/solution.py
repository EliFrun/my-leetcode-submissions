class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        l, h = min(num1, num2), max(num1, num2)
        ret = 0
        while l > 0:
            if h- l > l:
                l, h = l, h- l
            else:
                l, h = h - l, l
            ret += 1
        return ret
