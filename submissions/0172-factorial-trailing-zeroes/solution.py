class Solution:
    def trailingZeroes(self, n: int) -> int:
        return sum([n // (5 ** i) for i in range(1,7)])
        
