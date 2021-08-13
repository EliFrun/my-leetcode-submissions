class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.helper(1, n, k)
    
    
    def helper(self, lower, upper, k):
        if k == 1:
            return [[x] for x in range(lower, upper + 1)]
        ret = []
        for i in range(lower, upper):
            ret.extend([i] + x for x in self.helper(i + 1, upper, k - 1))
                
        return ret
