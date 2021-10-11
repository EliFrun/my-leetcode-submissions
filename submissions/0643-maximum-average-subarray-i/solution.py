class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m =  sum(nums[:k])
        curr = m
        for i in range(len(nums) - k):
            curr += nums[i + k] - nums[i]
            m = max(m, curr)
            
        return m / k
        
