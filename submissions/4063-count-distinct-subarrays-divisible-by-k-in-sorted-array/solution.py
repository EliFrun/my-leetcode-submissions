class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        mod_pre = defaultdict(SortedList)
        mod_pre[0].add(-1)
        prefix = 0
        ret = 0
        
        cnt = 0
        curr = 0
        first_idx = -1
        for i,v in enumerate(nums):
            prefix += v
            if v == curr:
                cnt += 1
            else:
                c = curr
                for _ in range(cnt):
                    if c % k == 0:
                        ret += 1
                    c += curr
                first_idx = i
                cnt = 1
                curr = v
            ret += mod_pre[prefix % k].bisect_left(first_idx - 1)
            mod_pre[prefix % k].add(i)

        c = curr
        for i in range(cnt):
            if c % k == 0:
                print('baz')
                ret += 1
            c += curr

        return ret
        
