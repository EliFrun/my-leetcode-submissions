class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        num_parents = defaultdict(int)
        for p, c in edges:
            num_parents[c] += 1
        
        return [i for i in range(n) if not num_parents[i]]
        
