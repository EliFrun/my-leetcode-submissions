class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @functools.cache
        def solve(n):
            if n == len(nums) - 1:
                return True
            if  nums[n] == 0:
                return False
            if n + nums[n] >= len(nums) - 1:
                return True

            for i in range(nums[n], 0, -1):
                if solve(n + i):
                    return True

            return False
               
        return solve(0)
        
