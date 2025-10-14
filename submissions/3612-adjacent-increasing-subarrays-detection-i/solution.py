class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev = 0
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                if curr >= 2 * k:
                    return True
                if curr >= k and prev >= k:
                    return True
                prev = curr
                curr = 1
        
        if curr >= 2 * k:
            return True
        if curr >= k and prev >= k:
            return True
        return False
                    
