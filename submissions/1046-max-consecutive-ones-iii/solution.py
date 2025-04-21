class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        z = 0
        left, right = 0, 0
        ret = 0
        while right < len(nums):
            if z <= k:
                z += 1 - nums[right]
                right += 1
            else:
                z -= 1 - nums[left]
                left += 1
            if z <= k:
                ret = max(ret, right - left)

        while left < len(nums) and z > k:
            z -= 1 - nums[left]
            left += 1

        ret = max(ret, right - left)
        return ret

            
        
