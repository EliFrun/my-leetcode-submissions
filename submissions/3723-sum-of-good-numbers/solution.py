class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ret = 0
        for i in range(len(nums)):
            left = nums[i - k] if i - k >= 0 else 0
            right = nums[i + k] if i + k < len(nums) else 0
            ret += nums[i] if left < nums[i] and right < nums[i] else 0

        return ret
        
