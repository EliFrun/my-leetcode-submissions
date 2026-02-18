class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        curr = 1 & n
        while n:
            print(curr)
            if 1 & n != curr:
                return False
            curr = 1 ^ curr
            n >>= 1
        return True
        
