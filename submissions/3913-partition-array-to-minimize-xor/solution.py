class Solution:
    def minXor(self, nums: List[int], k: int) -> int:

        @cache
        def solve(left, i):
            if len(nums) < left:
                return float('inf')
            if i >= len(nums):
                return 0
            if left == 1:
                ret = 0
                for j in range(i, len(nums)):
                    ret ^= nums[j]
                return ret
            
            curr = 0
            ret = float('inf')
            for j in range(i, len(nums) - left + 1):
                curr ^= nums[j]
                ret = min(ret, max(curr, solve(left - 1, j + 1)))

            return ret

        return solve(k, 0)
        
