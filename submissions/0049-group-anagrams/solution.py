class Solution:
    def default():
        return []
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        foo = defaultdict(Solution.default)
        
        for s in strs:
            foo[''.join(sorted(s))].append(s)
            
            
        ret = []    
        for k,v in foo.items():
            ret.append(v)
            
        return ret
