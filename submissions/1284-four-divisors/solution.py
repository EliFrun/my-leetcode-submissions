sieve = [True] * 400
sieve[0] = False
sieve[1] = False
for i in range(2, len(sieve)):
    if not sieve[i]:
        continue
    for j in range(i + i, len(sieve), i):
        sieve[j] = False

primes = [i for i, x in enumerate(sieve) if x]

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            print(num)
            factors = []
            for p in primes:
                while num % p == 0:
                    factors.append(p)
                    num //= p
                if num == 1:
                    break
                if len(factors) > 3:
                    break
            if num != 1:
                factors.append(num)
            if len(factors) > 3:
                continue
            if len(set(factors)) == 1 and len(factors) == 3:
                    ret += 1 + factors[0] + factors[0] ** 2 + factors[0] ** 3
            elif len(set(factors)) == 2 and len(factors) == 2:
                ret += 1 + factors[0] + factors[1] + factors[0] * factors[1]
            else:
                continue
        return ret
                
            



