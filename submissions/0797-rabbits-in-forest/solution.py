class Solution:
    def default():
        return 0
    
    def numRabbits(self, answers: List[int]) -> int:
        d = defaultdict(Solution.default)
        
        for a in answers:
            d[a] += 1
            
         
        ret = 0
        for key, value in d.items():
            if value > key + 1:
                ret += (key + 1) * (value // (key + 1))
                if value % (key + 1) > 0:
                    ret += max(value % (key + 1), key + 1)
            else:
                ret += max(value, key + 1)
                
        
        
        return ret
