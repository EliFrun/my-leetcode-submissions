class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            for j in range(i + 1, len(nums)):
                ret += bisect_left(nums, nums[i] + nums[j]) - j - 1
        return ret
        
