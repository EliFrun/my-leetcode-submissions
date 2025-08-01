class Solution:
    def monkeyMove(self, n: int) -> int:
        return (1_000_000_007 + pow(2, n, 1_000_000_007) - 2) % 1_000_000_007
        
