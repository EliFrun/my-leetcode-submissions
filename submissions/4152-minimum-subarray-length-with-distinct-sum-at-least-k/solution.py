class Solution:
    def minLength(self, nums: List[int], k: int) -> int:

        d = defaultdict(int)
        s = 0
        left = 0
        ret = float('inf')
        for i, num in enumerate(nums):
            d[num] += 1
            if d[num] == 1:
                s += num
            while s >= k:
                ret = min(ret, i - left + 1)
                d[nums[left]] -= 1
                if d[nums[left]] == 0:
                    s -= nums[left]
                left += 1
        if ret == float('inf'):
            return -1
        return ret
            
        
