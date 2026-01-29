class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        g = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if int(sqrt(nums[i] + nums[j])) ** 2 == nums[i] + nums[j]:
                    g[i].append(j)

        @cache
        def solve(used, prev):
            if all((1 << i) & used for i in range(len(nums))):
                return 1
            ret = 0
            for nxt in g[prev]:
                if used & (1 << nxt):
                    continue
                ret += solve(used | (1 << nxt), nxt)
            return ret
        
        res = 0
        for i in range(len(nums)):
            res += solve(1 << i, i)

        c = Counter(nums)
        for k,v in c.items():
            res //= factorial(v)

        return res
