class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:

        def solve(v):
            return v // a + v // b - v // (a * b // gcd(a, b))

        l, r = 1, int(1e18)
        ret = -1
        while l <= r:
            middle = (l + r) // 2
            if solve(middle) < n:
                l = middle + 1
            else:
                ret = middle
                r = middle - 1
        return ret % 1_000_000_007
        
