class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        s = SortedList()
        d = {}
        ret = [-1] * len(rains)

        for i, rain in enumerate(rains):
            if rain == 0:
                s.add(i)
            else:
                if rain in d:
                    idx = d[rain]
                    s_idx = s.bisect_left(idx)
                    if s_idx >= len(s):
                        return []
                    else:
                        v = s.pop(s_idx)
                        ret[v] = rain 
                d[rain] = i

        for idx in s:
            ret[idx] = 1
        return ret
                    
        
