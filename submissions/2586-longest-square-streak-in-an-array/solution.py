class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        p = set(nums)
        m = {}
        for num in nums:
           if num ** 2 in p:
                m[num] = num ** 2
        
        @cache
        def solve(num):
            ret = 0
            while num:
                num = m.get(num, None)
                ret += 1
            return ret

        ret = 0
        for num in nums:
            ret = max(solve(num), ret)

        return ret if ret > 1 else -1


        
