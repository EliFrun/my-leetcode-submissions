class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        foo = [0]
        for i in nums:
            foo.append(foo[-1] + (1 if i == 1 else -1))
            
        d = defaultdict(lambda: [])
        
        for i, v in enumerate(foo):
            d[v].append(i)
            
            
        curr_max = 0
        if 0 in d:
            curr_max = max(curr_max, d[0][-1])
            
        for _, v in d.items():
            if len(v) == 1:
                continue
            
            curr_max = max(curr_max, v[-1] - v[0])
            
        return curr_max
        
        
