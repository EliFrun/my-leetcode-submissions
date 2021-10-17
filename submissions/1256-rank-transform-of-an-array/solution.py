class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}         
        for i, v in enumerate(sorted(list(set((arr))), reverse=True)): 
            d[v] = i
           
        a = len(d.keys())
        return [a - d[x] for x in arr]
