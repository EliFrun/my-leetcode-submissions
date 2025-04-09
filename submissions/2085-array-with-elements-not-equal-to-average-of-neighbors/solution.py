class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = nums[i//2] if i & 1 == 0 else nums[(len(nums) + i) // 2]
        return ret
        
