class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l,r,k,v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % 1_000_000_007
            
        ret = 0
        for num in nums:
            ret ^= num

        return ret
                
        
