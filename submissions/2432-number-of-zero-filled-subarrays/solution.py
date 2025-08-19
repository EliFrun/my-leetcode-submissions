class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        ret = 0
        for num in nums:
            if num == 0:
                cnt += 1
            else:
                ret += cnt * (cnt + 1) // 2
                cnt = 0

        ret += cnt * (cnt + 1) // 2
        
        return ret
        
