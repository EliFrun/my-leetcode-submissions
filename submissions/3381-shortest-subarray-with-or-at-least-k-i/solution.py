class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ret = float('inf')
        for i in range(len(nums)):
            v = 0
            for j in range(i, len(nums)):
                v |= nums[j]
                if v >= k:
                    ret = min(ret, j - i + 1)
                    break

        return ret if ret != float('inf') else -1
                
        
