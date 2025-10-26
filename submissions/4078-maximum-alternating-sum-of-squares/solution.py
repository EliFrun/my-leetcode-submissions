class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x:x ** 2)
        i = 0
        j = len(nums) - 1
        ret = 0
        while i <= j:
            ret += nums[j] ** 2
            ret -= nums[i] ** 2
            i += 1
            j -= 1
        
        if len(nums) & 1:
            ret += nums[len(nums)//2] ** 2
        return ret

        
