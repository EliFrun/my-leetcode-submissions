class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return reduce(lambda t, x: t * int(x), str(n), 1) - sum([int(x) for x in str(n)])
        
