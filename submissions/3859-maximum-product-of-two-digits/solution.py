class Solution:
    def maxProduct(self, n: int) -> int:
        return prod(sorted([int(x) for x in str(n)])[len(str(n)) - 2:])
        
