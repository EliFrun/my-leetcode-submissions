class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        @cache
        def solve(v):
            for i in range(k - 1):
                v = bin(v).count('1')
            return v == 1

        ret = 0
        pre = 0
        for i,c in enumerate(s):
            if c == '1':
                for j in range(0 if pre else 1, len(s) - i):
                    if solve(j + pre):
                        ret = (ret + comb(len(s) - i - 1, j)) % 1_000_000_007
                pre += 1
        return ret
        
