class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        edge_map = defaultdict(set)
        for p, c in edges:
            edge_map[p].add(c)
            edge_map[c].add(p)

        odd_edges = []
        for edge, adj in edge_map.items():
            if len(adj) % 2 != 0:
                odd_edges.append(edge)

        
        if len(odd_edges) % 2 != 0:
            return False

        if len(odd_edges) > 4:
            return False

        if len(odd_edges) == 0:
            return True
        
        if len(odd_edges) == 2:
            return not odd_edges[0] in edge_map[odd_edges[1]] or len(
                set(
                    [i for i in range(1, n + 1)]).difference(edge_map[odd_edges[0]]).difference(edge_map[odd_edges[1]])) > 0



        if odd_edges[1] not in edge_map[odd_edges[0]] and odd_edges[2] not in edge_map[odd_edges[3]]:
            return True

        if odd_edges[2] not in edge_map[odd_edges[0]] and odd_edges[1] not in edge_map[odd_edges[3]]:
            return True

        if odd_edges[3] not in edge_map[odd_edges[0]] and odd_edges[1] not in edge_map[odd_edges[2]]:
            return True

        
        return False
            
        
