class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        v = list(Counter(nums).values()); m = max(v)
        return sum([x for x in v if x == m])
        
