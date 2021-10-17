class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(lambda: [[]])
        
        for i,v in enumerate(groupSizes):
            if len(d[v][-1]) < v:
                d[v][-1].append(i)
            else:
                d[v].append([i])
                
        ret = []
        for _,v in d.items():
            ret += v
                
        return ret
        
