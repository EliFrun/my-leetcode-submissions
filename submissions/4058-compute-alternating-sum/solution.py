class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum([x * (1 - 2 * (i & 1)) for i,x in enumerate(nums)])
        
