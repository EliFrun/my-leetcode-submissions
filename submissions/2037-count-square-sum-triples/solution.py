class Solution:
    def countTriples(self, n: int) -> int:
        ret = 0
        for a in range(1, n - 1):
            for b in range(a, n):
                foo = (a ** 2 + b ** 2) ** 0.5
                if foo <= n and foo.is_integer():
                    ret += 2
                        
        return ret
        
