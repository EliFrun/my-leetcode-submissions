class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        g1 = defaultdict(set)
        for p, c in edges1:
            g1[p].add(c)
            g1[c].add(p)

        g2 = defaultdict(set)
        for p, c in edges2:
            g2[p].add(c)
            g2[c].add(p)

        best = 0
        for i in g2.keys():
            curr = {i,}
            visited = set()
            layer = 0
            while curr and layer < k - 1:
                layer += 1
                nxt = set()
                for n in curr:
                    if n in visited:
                        continue
                    visited.add(n)
                    nxt |= g2[n]

                curr = nxt - visited
            best = max(best, len(visited | curr))

        if k == 0:
            best = 0

        ret = [0] * (max(g1.keys()) + 1)
        for i in range(len(ret)):
            curr = {i,}
            visited = set()
            layer = 0
            while curr and layer < k:
                layer += 1
                nxt = set()
                for n in curr:
                    if n in visited:
                        continue
                    visited.add(n)
                    nxt |= g1[n]

                curr = nxt - visited
            ret[i] = len(visited | curr) + best
        
        return ret

        

        
