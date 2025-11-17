class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        ret = 0
        for v in nums:
            if v == 1:
                cnt += 1
            else:
                ret = max(ret, cnt)
                cnt = 0
        ret = max(ret, cnt)
        return ret
        
