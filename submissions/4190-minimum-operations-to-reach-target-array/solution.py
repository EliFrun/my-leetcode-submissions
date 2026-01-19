class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        return len(set([x for x,y in zip(nums, target) if x != y]))
        
