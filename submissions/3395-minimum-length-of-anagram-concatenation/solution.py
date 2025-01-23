class Solution:
    def minAnagramLength(self, s: str) -> int:
        def prime_factors(n):
            if n <= 3:
                return [n]

            m = int(sqrt(n))
            for i in range(2, m + 1):
                if n // i == n / i:
                    return [i] + prime_factors(n // i)
            return [n]

        def generate_factors(primes):
            if len(primes) == 0:
                return [1]
            
            return generate_factors(primes[1:])  + [x * primes[0] for x in generate_factors(primes[1:])]


        def subdivide(n):
            return [''.join(sorted(list(s[i: i + n]))) for i in range(0, len(s), n)]

        factors = sorted(
            list(
                set(
                    generate_factors(
                        prime_factors(
                            len(s)
                        )
                    )
                )
            )
        )
        

        for p in factors:
            f = subdivide(p)
            print([len(x) for x in f])
            if all(x == f[0] for x in f):
                return len(f[0])

        return len(s)
        
