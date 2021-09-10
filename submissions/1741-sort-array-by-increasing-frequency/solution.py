class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = defaultdict(lambda: 0)
        
        for num in nums:
            d[num] += 1
            
        f = [(k, v) for k,v in d.items()]
        
        f.sort(key= lambda x: (x[1], -x[0]))
        
        ret = []
        for k, v in f:
            ret.extend([k] * v)
            
        return ret
