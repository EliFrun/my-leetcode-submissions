class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ret = 1
        curr = nums[0] - k
        for v in nums[1:]:
            if curr + 1 <= v + k:
                curr = max(curr + 1, v - k)
                ret += 1
        return ret
        
