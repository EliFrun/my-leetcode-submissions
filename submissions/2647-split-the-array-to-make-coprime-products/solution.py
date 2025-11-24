sieve = [True] * (1000000 + 1)
sieve[0] = False
sieve[1] = False
for i in range(2, 1001):
    if not sieve[i]:
        continue
    for j in range(i + i, len(sieve), i):
        sieve[j] = False
primes = [i for i,x in enumerate(sieve) if x]

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        def to_prime(num):
            c = defaultdict(int)
            for p in primes:
                while num % p == 0:
                    c[p] += 1
                    num //= p
                if num == 1:
                    break
                if sieve[num]:
                    c[num] += 1
                    break
            return c
        
        nums = [to_prime(num) for num in nums]
        

        right = Counter()
        for i, num in enumerate(nums):
            for k,v in num.items():
                right[k] += v

        common = set()
        for i in range(len(nums) - 1):
            for k,v in nums[i].items():
                common.add(k)
                right[k] -= v
                if right[k] == 0:
                    common.remove(k)
            if not common:
                return i
        return -1

        
