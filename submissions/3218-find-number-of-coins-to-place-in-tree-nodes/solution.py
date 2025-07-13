class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        g = defaultdict(set)
        for p, c in edges:
            g[p].add(c)
            g[c].add(p)

        ret = [0] * len(cost)
        visited = set()
        @cache
        def solve(n):
            visited.add(n)
            lis = g[n]
            g[n] = []
            negs = []
            pos = []
            if cost[n] < 0:
                negs.append(cost[n])
            else:
                pos.append(cost[n])
            for node in lis:
                if node in visited:
                    continue
                ne,po = solve(node)
                negs += ne
                pos += po

            if len(negs) + len(pos) < 3:
                ret[n] = 1
            else:
                negs.sort()
                negs = negs[:3]
                pos.sort()
                pos = pos[-3:]
                v = 0
                if len(pos) == 3:
                    v = max(v, pos[0] * pos[1] * pos[2])
                if len(negs) > 1 and pos:
                    v = max(v, negs[0] * negs[1] * pos[-1])
                ret[n] = v
            return (negs, pos)

        solve(0)
        return ret
        
