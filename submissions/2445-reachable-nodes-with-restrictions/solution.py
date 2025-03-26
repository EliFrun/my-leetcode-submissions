class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = defaultdict(set)
        for n1, n2 in edges:
            g[n1].add(n2)
            g[n2].add(n1)

        restricted = set(restricted)
        curr = set([0])
        visited = set()
        while curr:
            nxt = set()
            for n in curr:
                visited.add(n)
                nxt = nxt.union(g[n]).difference(visited).difference(restricted)

            curr = nxt

        return len(visited)
        
