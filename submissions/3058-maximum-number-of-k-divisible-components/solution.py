class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = defaultdict(list)

        for p, c in edges:
            g[p].append(c)
            g[c].append(p)

        good = 0
        def solve(parent, curr):
            nonlocal good
            s = values[curr]
            for c in g[curr]:
                if c == parent:
                    continue
                s += solve(curr, c)
            if s % k == 0:
                good += 1
            return s
        
        solve(None, 0)
        return good
        
