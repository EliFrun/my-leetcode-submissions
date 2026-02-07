class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        mins = [[1e9] * 2 for _ in range(len(nums))]
        
        l = 1e10
        for i, num in enumerate(nums):
            mins[i][0] = l
            if l > num:
                l = num

        r = 1e10
        for i in range(len(nums) - 1, -1, -1):
            mins[i][1] = r
            if r > nums[i]:
                r = nums[i]
        
        ret = 1e10
        for i, (l,r) in enumerate(mins):
            if ret > nums[i] + l + r and l < nums[i] and r < nums[i]:
                ret = nums[i] + l + r
        
        return ret if ret != 1e10 else -1
