class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        mProf = 0
        
        for i in prices:
            mProf = max(mProf, i - minPrice)
            minPrice = min(minPrice, i)
            
        return mProf
