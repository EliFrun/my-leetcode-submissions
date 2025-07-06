class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        c = Counter(nums)
        if k == 1:
            return max([-1] + [x for x, v in c.items() if v < 2])
            
        ret = -1
        if c[nums[0]] == 1:
            ret = max(ret, nums[0])
        if c[nums[-1]] == 1:
            ret = max(ret, nums[-1])
        
        return ret
