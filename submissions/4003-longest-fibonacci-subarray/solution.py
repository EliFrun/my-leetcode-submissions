class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ret = 2
        curr = 2
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] + nums[i - 2]:
                curr += 1
            else:
                ret = max(ret, curr)
                curr = 2

        ret = max(ret, curr)

        return ret
                
        
