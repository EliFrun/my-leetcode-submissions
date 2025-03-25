class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum([x for i,x in enumerate(nums) if bin(i)[2:].count('1') == k])
        
