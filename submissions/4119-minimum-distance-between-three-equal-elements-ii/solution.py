class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)

        ret = float('inf')
        for k,l in d.items():
            if len(l) < 3:
                continue
            for i in range(len(l) - 2):
                ret = min(ret, abs(l[i] - l[i + 1]) + abs(l[i + 1] - l[i + 2]) + abs(l[i] - l[i + 2]))

        if ret == float('inf'):
            return -1
        return ret
