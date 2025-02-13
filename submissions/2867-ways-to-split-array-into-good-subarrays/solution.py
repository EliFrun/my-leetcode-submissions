class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        pre = []
        count = 0
        found = False
        for n in nums:
            if n == 1:
                found = True
                pre.append(count)
                count = 0
            else:
                count += 1

        if not found:
            return 0


        ret = 1
        for p in pre[1:]:
            ret = (ret * (p + 1)) % 1_000_000_007

        return ret
        
