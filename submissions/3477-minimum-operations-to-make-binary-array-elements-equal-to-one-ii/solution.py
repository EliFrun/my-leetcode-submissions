class Solution:
    def minOperations(self, nums: List[int]) -> int:
        not_nums = [1-x for x in nums]
        def solve(i, inv):
            nonlocal not_nums
            n = nums if not inv else not_nums

            if i >= len(nums):
                return -1
            
            if i == len(nums) - 1:
                return  1 - n[-1]
    
            while i < len(nums) and n[i] == 1:
                i += 1


            return 1 + solve(i, not inv)
        
        return solve(0, False)
            
        
