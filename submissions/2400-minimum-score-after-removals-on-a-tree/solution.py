class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:        
        g = defaultdict(set)
        for p,c in edges:
            g[p].add(c)
            g[c].add(p)

        curr = set([0])
        visited = set()
        
        # we will create directed tree
        g2 = defaultdict(set)
        while curr:
            nxt = set()
            for c in curr:
                if c in visited:
                    continue
                visited.add(c)
                g2[c] = g[c] - visited
                nxt |= g[c] - visited

            curr = nxt - visited

        @cache
        def xor_sum(node):
            ret = nums[node]
            for c in g2[node]:
                ret ^= xor_sum(c)

            return ret

        @cache
        def downstream(node):
            ret = set([node])
            for c in g2[node]:
                ret.add(c)
                ret |= downstream(c)
            return ret

        res = float('inf')
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                p1, c1 = edges[i]
                if p1 in downstream(c1):
                    p1, c1 = c1, p1
                p2, c2 = edges[j]
                if p2 in downstream(c2):
                    p2, c2 = c2, p2


                if p1 in downstream(c2): # p1 tree is downstream of p2
                    l1 = xor_sum(0) ^ xor_sum(c2)
                    l2 = xor_sum(c2) ^ xor_sum(c1)
                    l3 = xor_sum(c1)
                    mi, ma = min(l1,l2,l3), max(l1,l2,l3)
                    res = min(res, ma - mi)
                elif p2 in downstream(c1): # p2 tree is downsteam of p1
                    l1 = xor_sum(0) ^ xor_sum(c1)
                    l2 = xor_sum(c1) ^ xor_sum(c2)
                    l3 = xor_sum(c2)
                    mi, ma = min(l1,l2,l3), max(l1,l2,l3)
                    res = min(res, ma - mi)
                else: # seperate branches
                    l1 = xor_sum(0) ^ xor_sum(c1) ^ xor_sum(c2)
                    l2 = xor_sum(c1)
                    l3 = xor_sum(c2)
                    
                mi, ma = min(l1,l2,l3), max(l1,l2,l3)
                res = min(res, ma - mi)
                

        return res




        

        
