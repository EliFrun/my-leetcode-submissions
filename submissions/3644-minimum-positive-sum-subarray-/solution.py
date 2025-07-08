class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ret = float('inf')
        for i in range(len(nums) - l + 1):
            s = 0
            for j in range(i, min(i + r, len(nums))):
                s += nums[j]
                if j - i + 1 >= l:
                    if s > 0:
                        ret = min(ret, s)

        return ret if ret != float('inf') else -1
        
