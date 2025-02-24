class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        edge_map = [[] for _ in range(len(amount))]
        for n1, n2 in edges:
            edge_map[n1].append(n2)
            edge_map[n2].append(n1)

        def dfs(prev, curr, target):
            if curr == target:
                return [curr]

            ret = []
            for n in edge_map[curr]:
                if n != prev:
                    if v := dfs(curr, n, target):
                        ret = [curr]
                        ret.extend(v)
                        break
            return ret

        path = dfs(None, bob, 0)
        if len(path) % 2 != 0:
            amount[path[len(path)//2]] //= 2
        for n in path[:len(path)//2]:
            amount[n] = 0

        def best_dfs(prev, curr):
            ret = amount[curr]
            best_val = -1_000_000_000_000
            for n in edge_map[curr]:
                if n != prev:
                    best_val = max(best_val, best_dfs(curr, n))
            return ret + (best_val if best_val != -1_000_000_000_000 else 0)

        return best_dfs(None, 0)


        
