class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = [[] for _ in range(max(nums) + 1)]
        for i,v in enumerate(nums):
            d[v].append(i)

        ret = 0
        for v in d:
            for i in range(len(v)):
                for j in range(i + 1, len(v)):
                    a,b = v[i], v[j]
                    ret += (1 if (a * b) % k == 0 else 0)

        return ret
