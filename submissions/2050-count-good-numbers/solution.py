class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(5, (n+1)//2, 1_000_000_007) * pow(4,n//2, 1_000_000_007)) % 1_000_000_007
        
