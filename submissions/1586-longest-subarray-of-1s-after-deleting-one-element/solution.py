class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        ret = 0
        count = 0
        curr = 0
        for i, num in enumerate(nums):
            if num == 0:
                count += 1
            else:
                curr += 1
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                else:
                    curr -= 1
                left += 1
            ret = max(ret, curr - (1 if count == 0 else 0))

        return ret

        
