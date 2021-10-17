class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        a, b = 0, sum(nums)
        
        for i, v in enumerate(nums):
            if a == b - v:
                return i
             
            a += v
            b -= v
        return -1
