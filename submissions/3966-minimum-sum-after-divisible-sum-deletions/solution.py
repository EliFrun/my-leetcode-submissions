class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        best_mod = {}
        best_mod[0] = 0
        prefix = 0
        best = 0
        for i,v in enumerate(nums):
            prefix += v
            if prefix % k not in best_mod:
                best_mod[prefix % k] = best + v
            else:
                best_mod[prefix % k] = min(best_mod[prefix % k], best + v)
            best = min(best + v, best_mod[prefix % k])
        return best
        
