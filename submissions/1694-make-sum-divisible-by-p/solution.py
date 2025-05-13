class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        d = sum(nums) % p
        if d == 0:
            return 0
        
        cs = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            cs[i + 1] = num + cs[i]

        m = defaultdict(SortedList)
        for i, x in enumerate(cs):
            m[x % p].add(i)

        ret = float('inf')
        for k,v in m.items():
            for i in v:
                t = (k - d + p) % p
                if t not in m:
                    continue
                idx = min(m[t].bisect_left(i) - 1, len(m[t]) - 1)
                if idx >= 0:
                    ret = min(ret, i - m[t][idx])

        return ret if ret < len(nums) else -1

        

        


        
