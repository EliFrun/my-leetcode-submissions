class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:


        g = defaultdict(list)
        m = 0
        for p,c,a in conversions:
            m = max(m,p,c)
            g[p].append((c,a))
            g[c].append((p, 1/a))

        l = [0] * (1 + m)
        l[0] = 1
        q = deque([0])

        while q:
            curr = q.pop()
            for c, a in g[curr]:
                if l[c] != 0:
                    continue
                l[c] = (l[curr] * a) % 1_000_000_007
                q.appendleft(c)

        return l
