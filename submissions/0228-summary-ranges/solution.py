class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ret = []
        mi = nums[0]
        ma = nums[0]
        for n in nums[1:]:
            if n == ma + 1:
                ma += 1
            else:
                ret.append(f'{mi}->{ma}' if ma - mi >= 1 else str(mi))
                mi, ma = n, n

        ret.append(f'{mi}->{ma}' if ma - mi >= 1 else str(mi))
        
        return ret
        
