class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        idx = len(nums) // 2
        bound = bisect_left(nums, k)
        l, r = min(idx, bound), max(idx, bound)
        if k < nums[idx]:
            r += 1

        return sum([abs(x - k) for x in nums[l:r]])
        
