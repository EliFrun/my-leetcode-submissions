class Solution:
    def maxNiceDivisors(self, p: int) -> int:
        return p if p <= 3 else (4 if p % 3 == 1 else (1 if p % 3 == 0 else 2)) * pow(3, p//3 - (1 if p % 3 == 1 else 0), 1_000_000_007) % 1_000_000_007
        
