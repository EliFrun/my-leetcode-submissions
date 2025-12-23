class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(a, b):
            return a * b // gcd(a,b)

        def solve(v):
            return v // a + v // b + v // c + v // (lcm(a, lcm(b,c))) - v // (a * b // gcd(a,b))  - v // (b * c // gcd(b,c)) - v // (a * c // gcd(a, c))

        

        l, r = 1, n * a * b * c
        ret = -1
        while l <= r:
            middle = (l + r) // 2
            if solve(middle) < n:
                l = middle + 1
            else:
                ret = middle
                r = middle - 1
        return ret
        
        
