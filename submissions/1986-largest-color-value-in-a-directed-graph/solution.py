class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for p,c in edges:
            if p == c:
                return -1
            g[p].add(c)

        cycle_detected = False
        @cache
        def dfs(i):
            nonlocal cycle_detected
            if cycle_detected:
                return -1
            if g[i] == False:
                cycle_detected = True
                return -1
            prev = g[i]
            g[i] = False
            ret = [0] * 26
            for n in prev:
                x = dfs(n)
                if x == -1:
                    return -1
                for idx, v in enumerate(x):
                    ret[idx] = max(ret[idx], v)
            g[i] = prev
            ret[ord(colors[i]) - ord('a')] += 1
            return ret

        ret = -1
        for j in range(len(colors)):
            v = dfs(j)
            if dfs(j) == -1:
                return -1
            ret = max(ret, max(v))

        return ret
        
        

        


