class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        def primes(n):
            nums = [True] * (int(sqrt(n)) + 2)
            for i in range(2, len(nums)):
                if nums[i]:
                    for j in range(2 * i, len(nums), i):
                        nums[j] = False
            
            return [i for i,v in enumerate(nums) if i > 1 and v]
        
        m = max(nums)
        p = primes(m)
        

        @cache
        def score(n):
            ret = 0
            for i in p:
                if i > n:
                    break
                if n % i == 0:
                    ret += 1
                while n % i == 0:
                    n //= i
            if n > 1:
                ret += 1
            return ret

        
        scores = [(x, score(x)) for x in nums]
        left = [(-1, 1_000_000_000)]
        combos = [[0,0] for _ in range(len(nums))]
        for i, (x, score) in enumerate(scores):
            while left[-1][1] < score:
                left.pop()

            combos[i][0] = i - left[-1][0]
            left.append((i, score))

        right = [(len(nums), 1_000_000_000)]
        for i in range(len(nums) - 1, -1, -1):
            x, score = scores[i]
            while right[-1][1] <= score:
                right.pop()
            
            combos[i][1] = right[-1][0] - i
            right.append((i, score))


        combos = [x*y for x,y in combos]



        lis = sorted((-v, -combo) for v, combo in zip(nums, combos))
        ret = 1
        for v, combo in lis:
            ret = ret * pow(-v, min(k, -combo), MOD) % MOD

            k += combo
            if k <= 0:
                break

        return ret

                



        
