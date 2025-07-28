class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        best = 0
        for num in nums:
            best |= num
       
        @cache
        def solve(incoming, i):
            if i >= len(nums):
                return 1 if incoming == best else 0
            
            return solve(incoming | nums[i], i + 1) + solve(incoming, i + 1)

        return solve(0, 0)
