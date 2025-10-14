class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        curr = SortedList()
        left = 0
        ret = 0
        for i, num in enumerate(nums):
            curr.add(num)
            while curr[-1] - curr[0] > limit:
                curr.remove(nums[left])
                left += 1
            ret = max(ret, i - left + 1)
        return ret
        
