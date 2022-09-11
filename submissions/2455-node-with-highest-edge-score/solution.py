class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        d = defaultdict(int)
        for idx, val in enumerate(edges):
            d[val] += idx
            
        return max(d.items(), key=lambda x: (x[1], -x[0]))[0]
            
            
        
