class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for p, c in roads:
            graph[p].append(c)
            graph[c].append(p)

        cost = 0
        
        visited = set()
        def dfs(node):
            nonlocal graph
            nonlocal cost
            nonlocal visited
            new_nodes = [x for x in graph[node] if x not in visited]
            if len(new_nodes) == 0:
                return 1

            visited.add(node)
            
            people = [dfs(x) for x in new_nodes]
            cost += sum([ceil(p/seats) for p in people])
            return 1 + sum(people)


        dfs(0)
        return cost


        
        
