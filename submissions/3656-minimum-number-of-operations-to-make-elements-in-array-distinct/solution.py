class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        g = set([k for k,v in c.items() if v >= 2])
        ret = 0
        i = 0
        while g:
            lis = nums[i:i + 3]
            for n in lis:
                c[n] -= 1
                if c[n] < 2 and n in g:
                    g.remove(n)
            i += 3
            ret += 1

        return ret

        
        
