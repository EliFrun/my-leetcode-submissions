class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        def primes(n):
            if n < 3:
                return 0
            nums = list(range(2, n))
            curr = nums[0]
            while curr < sqrt(n):
                for i in range(curr + curr, n, curr):
                    nums[i - 2] = 0
                found = False
                for i in range(curr + (1 if curr & 1 == 0 else 2), int(sqrt(n)) + 1, 2):
                    if nums[i - 2] > 1:
                        found = True
                        curr = nums[i - 2]
                        break
                if not found:
                    break
            return [x for x in nums if x > 0]
        
        prime = primes(maxValue + 1)
        @cache
        def factors(v):
            if v == 1:
                return []
            for p in prime:
                if v % p == 0:
                    return [p] + factors(v // p)

            return [v]

        def possible_lists(l):
            ret = [[]]
            for v in l:
                new = []
                for i in range(0, v + 1):
                    for r in ret:
                        new.append(r + [i])
                ret = new
            return ret

        def solve(v):
            if v == 1:
                return 1
            ret = 1
            for v in Counter(factors(v)).values():
                ret *= comb(n + v - 1, v)
            return ret


        return sum(solve(v) for v in range(1, maxValue + 1)) % 1_000_000_007


            
        
