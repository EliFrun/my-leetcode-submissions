class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        ret = 0
        for i in nums[:-1]:
            left += i
            right -= i

            if left >= right:
                ret += 1

        return ret
        
