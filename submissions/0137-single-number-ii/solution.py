class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return - (sum(nums) - 3 * sum(list(set(nums)))) // 2
        
