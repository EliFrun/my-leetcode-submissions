class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        bits = 0
        n = max(nums)
        while n > 0:
            bits += 1
            n >>= 1
        ret = 0
        for i in range(32, -1, -1):
            nums.sort(reverse=True)
            if nums[m - 1] >= 1 << i:
                ret |= 1 << i
                nums = [x & ((1 << i) - 1) for x in nums if x >= 1 << i]
            else:
                needed = 0
                for j in range(m):
                    needed += max(0, (1 << i) - nums[j])
                if needed <= k:
                    for j in range(m):
                        if nums[j] < (1<<i):
                            nums[j] = 1 << i
                    k -= needed
                    ret |= 1 << i
                    nums = [x & ((1 << i) - 1) for x in nums if x >= 1 << i]
                else:
                    nums = [x & ((1 << i) - 1) for x in nums]
                    
        
        return ret

        
        
