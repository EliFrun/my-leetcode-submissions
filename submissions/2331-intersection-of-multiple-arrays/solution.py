class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s = set(nums[0])
        for l in nums[1:]:
            s &= set(l)
        return sorted(list(s))
        
