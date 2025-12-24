class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        vals = SortedList(nums[:k])
        ret = []
        for i, num in enumerate(nums):
            if i < k:
                continue
            ret.append(vals[-1])
            vals.remove(nums[i - k])
            vals.add(num)
        ret.append(vals[-1])
        return ret
            
        
