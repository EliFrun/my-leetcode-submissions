class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_map = defaultdict(int)
        for n1, n2 in edges:
            edge_map[n1] += 1
            edge_map[n2] += 1

        return [k for k, v in edge_map.items() if v > 1][0]
        
