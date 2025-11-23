class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        ret = 0
        even_cnt, odd_cnt = 0, 0
        seen = {(0, 0): -1 }
        curr = 0
        for i, num in enumerate(nums):
            curr ^= num
            even_cnt += 1 - (num & 1)
            odd_cnt += num & 1
            if (even_cnt - odd_cnt, curr) in seen:
                ret = max(ret, i - seen[(even_cnt - odd_cnt, curr)])
            if (even_cnt - odd_cnt, curr) not in seen:
                seen[(even_cnt - odd_cnt, curr)] = i
        return ret
        
