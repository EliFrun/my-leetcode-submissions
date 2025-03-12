class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        g = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    g[nums[i]].append(nums[j])
        
        @cache
        def dfs(i):
            nonlocal g
            m = 0
            ret = []
            for n in g[i]:
                r = dfs(n)
                if len(r) > m:
                    m = len(r)
                    ret = r
            return [i] + ret
        
        m = 0
        ret = []
        for num in nums:
            r = dfs(num)
            if len(r) > m:
                m = len(r)
                ret = r

        return ret
