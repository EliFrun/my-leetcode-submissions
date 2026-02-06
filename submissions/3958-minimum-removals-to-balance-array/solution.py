class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        ret = len(nums)
        for i in range(len(nums)):
            ret = min(ret, i + max(0, (len(nums) - bisect_left(nums, nums[i] * k + 1))))
        return ret
        
