class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        pp = list(range(len(vals)))

        def find(v):
            if pp[v] == v:
                return v
            res = find(pp[v])
            pp[v] = res
            return res

        def union(u, v):
            uu = find(u)
            vv = find(v)
            pp[uu] = vv

        s = sorted([(v, i) for i,v in enumerate(vals)])

        g = defaultdict(list)
        for p,c in edges:
            if vals[p] > vals[c]:
                g[p].append(c)
            else:
                g[c].append(p)

        curr_v = s[0][0]
        curr = set([s[0][1]])
        ret = 0
        for v, i in s[1:] + [(float('inf'), 1e9)]:
            if v == curr_v:
                curr.add(i)
            else:
                for j in curr:
                    for c in g[j]:
                        union(j, c)
                d = defaultdict(set)
                for j in curr:
                    d[find(j)].add(j)
                
                for k,l in d.items():
                    ret += len(l) + (len(l) * (len(l) - 1)) // 2
                
                curr_v = v
                curr = set([i])
        return ret
   
