class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(lambda: 0)
        
        for i in nums:
            d[i] += 1
            
        foo = 0
        ret = 0
        
        
        for key, value in d.items():
            if value > foo:
                foo = value
                ret = key
            
                
        return ret
        
