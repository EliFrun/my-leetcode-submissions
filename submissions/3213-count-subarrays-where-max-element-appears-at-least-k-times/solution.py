class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        c = []
        ret = 0
        m = max(nums)
        for i, num in enumerate(nums):
            if num == m:
                c.append(i)
            ret += c[-k] + 1 if len(c) >= k else 0
        
        return ret
