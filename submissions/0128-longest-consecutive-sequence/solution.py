class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ret = 0
        @cache
        def solve(v):
            if v not in s:
                return 0
            nonlocal ret
            res = 1 + solve(v + 1)
            if res > ret:
                ret = res
            return res
        for v in s:
            solve(v)
        return ret

        
        
