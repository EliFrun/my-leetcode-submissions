class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        # counts
        curr = [
            [0,0], # even_parity cnt 1, even_parity cnt 2
            [0,0] # odd parity cnt 1, odd_parity cnt 2
        ]
        ret = 0
        for i in range(len(nums)):
            p = nums[i] % 2
            curr[p][1] = (curr[p][1] + curr[p][0]) % 1_000_000_007
            curr[p][0] = (curr[p][0] + 1 + sum(curr[1 - p])) % 1_000_000_007
        return sum(sum(x) for x in curr) % 1_000_000_007
            
            
            
        
