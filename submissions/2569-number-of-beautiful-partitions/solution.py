class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        primes = '2357'
        if s[0] not in primes or s[-1] in primes:
            return 0

        divides = [-1]
        for i in range(len(s) - 1):
            if s[i] not in primes and s[i + 1] in primes:
                divides.append(i)

        while divides[-1] + minLength >= len(s):
            divides.pop()

        @cache
        def solve(i, left):
            if left == 0:
                return 1
            if len(divides) - i < left:
                return 0
            if i >= len(divides):
                return 0
            
            next_i = bisect_left(divides, divides[i] + minLength)
            return sum(solve(i, left - 1) for i in range(next_i, len(divides)))

        return solve(0, k - 1) % 1_000_000_007
