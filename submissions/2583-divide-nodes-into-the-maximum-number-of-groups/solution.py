class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for p,c in edges:
            graph[c].add(p)
            graph[p].add(c)

        graphs = []
        visited = set()
        for i in range(1, n + 1):
            if i in visited:
                continue
            partitions = [set(), set()]
            part = 0
            curr = set([i])
            while curr:
                nxt = set()
                for c in curr:
                    for n in graph[c]:
                        if n in partitions[part]:
                            return -1
                        if n in partitions[1 - part]:
                            continue
                        nxt.add(n)

                partitions[part].update(curr)
                curr = nxt
                part = 1 - part

            visited.update(partitions[0])
            visited.update(partitions[1])
            graphs.append(partitions[0].union(partitions[1]))

        def bfs(node):
            nonlocal graph
            curr = set([node])
            visited = set()
            count = 0
            while curr:
                count += 1
                nxt = set()
                for c in curr:
                    visited.add(c)
                    for n in graph[c]:
                        if n in visited:
                            continue
                        nxt.add(n)

                curr = nxt

            return count

        ret = 0
        for g in graphs:
            ret += max([bfs(node) for node in g])

        return ret




    

        
       
