class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = min(nums)
        ret = sum([num - m for num in nums])
        return ret

        
