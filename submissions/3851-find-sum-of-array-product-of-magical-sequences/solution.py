class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        MOD = 1_000_000_007
        def factorial(v):
            ret = 1
            for i in range(1, v + 1):
                ret *= i
            return ret

        @cache
        def solve(m, i, k_left, bits):
            k = k_left + bin(bits).count('1')
            if K - k > M - m:
                return 0
            
            if m == M:
                return factorial(M) if k == K else 0
            
            if i >= len(nums):
                return 0

            ret = 0
            for c in range(M - m + 1):
                ret += nums[i] ** c * solve(m + c, i + 1, k_left + (bits & 1), bits >> 1) // factorial(c)
                bits += 1
            return ret
        return solve(0, 0, 0, 0) % MOD

            
            
        
