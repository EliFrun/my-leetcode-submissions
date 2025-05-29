class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        g1 = defaultdict(set)
        for p,c in edges1:
            g1[p].add(c)
            g1[c].add(p)

        g2 = defaultdict(set)
        for p,c in edges2:
            g2[p].add(c)
            g2[c].add(p)

        curr = set([0])
        visited = set()
        layer = 0
        even_odd1 = [-1] * (max(g1.keys()) + 1)
        counts = [0,0]
        while curr:
            nxt = set()
            for n in curr:
                counts[layer] += 1
                even_odd1[n] = layer
                visited.add(n)
                nxt |= g1[n]

            curr = nxt - visited
            layer = 1 - layer

        curr = set([0])
        visited = set()
        layer = 0
        even_odd2 = [0,0]
        while curr:
            even_odd2[layer] += len(curr)
            nxt = set()
            for n in curr:
                visited.add(n)
                nxt |= g2[n]

            curr = nxt - visited
            layer = 1 - layer

        best = max(even_odd2)

        return [
            counts[even_odd1[i]] + best 
            for i in range(max(g1.keys()) + 1)
        ]


        
        
