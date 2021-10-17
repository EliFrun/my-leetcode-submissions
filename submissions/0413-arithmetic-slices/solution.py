class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        diffs = [nums[i] - nums[i + 1] for i in range(0, len(nums) - 1)]
        curr = diffs[0]
        
        count = 1
        ret = 0
        for i in diffs[1:]:
            if i == curr:
                count += 1
            else:
                count += 1
                if count >= 3:
                    ret += (count - 2) * (count - 1) // 2
                count = 1
                curr = i
        
        count += 1
        ret += (count - 2) * (count - 1) // 2 if count >= 3 else 0
                
        return ret
        
