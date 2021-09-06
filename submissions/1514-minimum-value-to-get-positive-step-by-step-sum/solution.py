class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        m = 0
        c = 0
        
        for i in nums:
            c += i
            m = min(m, c)
            
        return - m + 1
