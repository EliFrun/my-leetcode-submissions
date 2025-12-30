class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        c = Counter(label)
        m = 0
        p1 = 0
        for k, v in c.items():
            if v & 1:
                p1 = 1
            m += 2 * (v // 2)
        m += p1
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        @cache
        def dfs(left_node, right_node, visited):
            ret = 0
            for i in g[left_node]:
                if (visited >> i) & 1:
                    continue
                for j in g[right_node]:
                    if (visited >> j) & 1:
                        continue
                    if i == j:
                        continue
                    if label[i] != label[j]:
                        continue
                    l, r = (i, j) if i < j else (j, i)
                    if (v := 2 + dfs(l, r, visited | (1 << i) | (1 << j))) > ret:
                        ret = v
            return ret

        res = 1
        for i in range(n):
            res = max(res, 1 + dfs(i, i, (1 << i)))
            for edge in g[i]:
                if edge < i:
                    continue
                if label[i] != label[edge]:
                    continue
                res = max(res, 2 + dfs(i, edge, (1 << i) | (1 << edge)))
                if res == m:
                    return res

        return res

        
                

            
        
