class Solution:
    def countPairs(self, c: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)

        seen = set()
        ret = 0
        for i in range(c):
            if i in seen:
                continue
            
            curr = set([i])
            visited = set()
            while curr:
                nxt = set()
                for n in curr:
                    if n in visited:
                        continue
                    visited.add(n)
                    nxt |= graph[n]

                curr = nxt - visited

            
            ret += len(visited) * (c - len(visited))
            seen |= visited

        return ret // 2
            


