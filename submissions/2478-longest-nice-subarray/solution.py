class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left,right = 0, 0
        curr = 0
        ret = 0
        while right < len(nums):
            if curr & nums[right] > 0:
                while curr & nums[right] != 0:
                    curr ^= nums[left]
                    left += 1
            else:
                ret = max(ret, right - left + 1)
            
            curr = curr | nums[right]
            right += 1

        return ret
