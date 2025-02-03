class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count_dec = 1
        count_inc = 1
        ret = 1
        for i in range(1,len(nums)):
            if nums[i - 1] < nums[i]:
                ret = max(count_dec, ret)
                count_inc += 1
                count_dec = 1
            elif nums[i - 1] > nums[i]:
                ret = max(count_inc, ret)
                count_dec += 1
                count_inc = 1
            else:
                ret = max(ret, count_dec, count_inc)
                count_dec = 1
                count_inc = 1

        return max(ret, count_inc, count_dec)
        
