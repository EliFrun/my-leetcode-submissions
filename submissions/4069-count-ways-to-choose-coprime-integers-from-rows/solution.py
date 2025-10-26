class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        sieve = [True] * max(max(x) + 1 for x in mat)
        for i in range(2, len(sieve)):
            if not sieve[i]:
                continue
            for j in range(2 * i, len(sieve), i):
                sieve[j] = False

        primes = [i for i, x in enumerate(sieve) if x and i > 1]

        def bit_mask(v):
            ret = 0
            for i, p in enumerate(primes):
                if v % p == 0:
                    ret |= 1 << i
            return ret

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = bit_mask(mat[i][j])

        @cache
        def solve(i, j, mask):
            if mask == 0:
                return pow(len(mat[0]), len(mat) - 1 - i, 1_000_000_007)
            if i == len(mat) - 1:
                return 1 if mask == 0 else 0
            return sum(
                solve(i + 1, k, mask & mat[i + 1][k]) for k in range(len(mat[0]))
            ) % 1_000_000_007
        return sum(solve(0, j, mat[0][j]) for j in range(len(mat[0]))) % 1_000_000_007

        


        
