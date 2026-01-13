class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        g = defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b)
            indegree[b] += 1


        # cycle detection
        for i in range(numCourses):
            visited = set()
            curr = set(g[i])
            while curr:
                nxt = set()
                for v in curr:
                    visited.add(v)
                    if v == i:
                        return []
                    nxt.update(g[v])
                curr = nxt - visited


        visited = [False] * numCourses
        stk = []
        for i in range(numCourses):
            if indegree[i]:
                continue
            stk.append(i)

        ret = []

        def dfs(n):
            nonlocal ret
            if visited[n]:
                return
            visited[n] = True
            for nxt in g[n]:
                dfs(nxt)
            ret.append(n)

        for v in stk:
            dfs(v)
        return ret

        
