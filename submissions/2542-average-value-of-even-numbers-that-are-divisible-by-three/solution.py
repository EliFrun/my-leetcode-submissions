class Solution:
    def averageValue(self, nums: List[int]) -> int:
        l = [x for x in nums if x % 2 == 0 and x % 3 == 0]
        return sum(l) // len(l) if len(l) > 0 else 0
        
