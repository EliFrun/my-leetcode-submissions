class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        ret = 0
        for v in nums[:-1]:
            left += v
            right -= v
            if (right - left) % 2 == 0:
                ret += 1
        return ret
        
