class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ret = 0
        prev = 0
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                ret = max(ret, min(curr, prev), curr // 2)
                prev = curr
                curr = 1
        
        return max(ret, min(curr, prev), curr // 2)
