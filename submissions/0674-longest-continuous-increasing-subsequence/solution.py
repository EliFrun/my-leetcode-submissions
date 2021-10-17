class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        m = 0
        curr = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                curr += 1
            else:
                m = max(curr, m)
                curr = 1
                
        return max(m, curr)
        
