class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0,1
        curr = nums[0]
        m = 1_000_000
        while right < len(nums):
            if curr < target:
                curr += nums[right]
                right += 1
            elif curr >= target:
                m = min(m, right - left)
                curr -= nums[left]
                left += 1

        while left < right and curr >= target:
            m = min(m, right - left)
            curr -= nums[left]
            left += 1

        return m if m != 1_000_000 else 0
        
