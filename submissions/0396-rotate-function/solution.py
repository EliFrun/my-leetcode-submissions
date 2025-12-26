class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = sum(nums)
        curr = sum([i * num for i, num in enumerate(nums)])
        ret = float('-inf')
        for i, v in enumerate(nums):
            curr += s
            curr -= (len(nums)) * nums[-i - 1]
            ret = max(ret, curr)
        return ret
        
        
