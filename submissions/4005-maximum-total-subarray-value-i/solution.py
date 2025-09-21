class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        ma = max(nums)
        mi = min(nums)
        return (ma - mi) * k
        
        
                
                
        
