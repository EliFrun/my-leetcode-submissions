class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        if not changed:
            return []
        
        changed.sort()
        vals = Counter(changed)
        
        ret = []
        for val in changed:
            if vals[val] > 0 and vals[2 * val] > 0:
                ret.append(val)
                vals[val] -= 1
                vals[2 * val] -= 1
                
        return ret if all([x == 0 for x in vals.values()]) else []
        
        
