class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(lambda: -1)
        for c, p in enumerate(edges):
            graph[c] = p

        c = [None] * len(edges)
        in_c = []
        def in_cycle(seq, n):
            if c[n] != None:
                return c[n]
            if graph[n] == -1:
                c[n] = False
                return False
            if n in seq:
                in_c.append(n)
                for node in seq:
                    c[n] = True
                return c[n]

            seq.add(n)
            ret = in_cycle(seq, graph[n])
            c[n] = ret
            return ret

        for i in range(len(edges)):
            in_cycle(set(), i)

        if not any(c):
            return -1

        ret = 0
        for n in in_c:
            curr = n
            visited = set()
            r = 1
            while True:
                visited.add(curr)
                curr = graph[curr]
                if curr in visited:
                    ret = max(ret, r)
                    break
                r += 1

        return ret

