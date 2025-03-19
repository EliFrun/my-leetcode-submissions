class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def solve(i, count):
            while i < len(nums) and nums[i] == 1:
                i += 1
            if i >= len(nums) - 2:
                return count if all([x == 1 for x in nums[i:]]) else -1
            
            for j in range(i, i + 3):

                nums[j] = 1 - nums[j]
            return solve(i + 1, count + 1)
        
        ret = solve(0, 0)
        return ret
        
