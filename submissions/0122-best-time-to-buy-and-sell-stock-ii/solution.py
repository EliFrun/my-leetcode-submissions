class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        
        curr = prices[0]
        
        for i in prices:
            if i < curr:
                curr = i
            if i > curr:
                prof += i - curr
                curr = i
                
        return prof
