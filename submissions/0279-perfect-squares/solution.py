class Solution:
    def numSquares(self, m: int) -> int:
        cache = [10 ** 5 for _ in range(m + 1)]
        def solve(n):
            if int(sqrt(n)) * int(sqrt(n)) == n:
                cache[n] = 1
                return cache[n]
            if cache[n] != 10 ** 5:
                return cache[n]
            
            if n <= 3:
                cache[n] = n
                return cache[n]
            
            cache[n] = min([ 1 + solve(n - i * i) for i in range(int(sqrt(n)), 0, -1) ])
            return cache[n]


        return solve(m)

        
