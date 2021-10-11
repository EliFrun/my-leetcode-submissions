class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if not changed:
            return []
        
        if len(changed) % 2 != 0:
            return []
        
        d = defaultdict(int)
        for i in changed:
            d[i] += 1
            
        if d[0] % 2 != 0:
            return []
         
        l = sorted(d.keys())
        j = 0
        ret = []
        for i in range(len(changed) // 2):
            while d[l[j]] == 0:
                j += 1
            
            if 2 * l[j] not in d or d[2 * l[j]] <= 0:
                return []
            else:
                ret += [l[j]]
                d[l[j]] -= 1
                d[2 * l[j]] -= 1
                
                
        return ret
