class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = nums[0]
        for v in nums[1:]:
            n &= v
        if n != 0:
            return 1
        
        cnt = 0
        i = 0
        n = nums[i]
        while i < len(nums):
            n &= nums[i]
            if n == 0:
                cnt += 1
                if i + 1 < len(nums):
                    n = nums[i + 1]
            i += 1
        return cnt
            

