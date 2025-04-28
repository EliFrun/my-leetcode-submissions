class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        curr = 0
        ret = 0
        while right < len(nums):
            if curr * (right - left) < k:
                print('foo')
                ret += right - left
                curr += nums[right]
                right += 1
            else:
                curr -= nums[left]
                left += 1

        while curr * (right - left) >= k:
           curr -= nums[left]
           left += 1 
        ret += right - left
        return ret
        
