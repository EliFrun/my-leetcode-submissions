class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        return int(''.join([x for x in str(n) if x != '0'])) * sum([int(x) for x in str(n)])
        
