primes = [True] * 40_000
primes[0] = False
primes[1] = False
for i in range(2, len(primes)):
    if not primes[i]:
        continue
    for j in range(i + i, len(primes), i):
        primes[j] = False
    
primes = [i for i,v in enumerate(primes) if v]

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # 2 * n = (k) * (x + (x + k + 1))
        factors = defaultdict(lambda: 1)
        for p in primes:
            while n % p == 0:
                n //= p
                factors[p] += 1
            if n == 1:
                break
        if n > 1:
            factors[n] += 1
        ret = 1
        for k,v in factors.items():
            if k == 2:
                continue
            ret *= v
        return ret
        
