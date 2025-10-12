class Solution:
    def sumDivisibleByK(self, nums: List[int], kk: int) -> int:
        c = Counter(nums)
        ret = 0
        for k,v in c.items():
            if v % kk == 0:
                ret += v * k
        return ret
        
