class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = sorted([x for x in set(nums)])
        return a[-3] if len(a) >= 3 else a[-1]
        
