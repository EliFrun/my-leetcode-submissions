class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        graphs = list(range(len(nums)))

        def find(v):
            if graphs[v] != v:
                graphs[v] = find(graphs[v])
            return graphs[v]
        
        for u,v in swaps:
            uu, vv = find(u), find(v)
            graphs[uu] = vv

        evens = 0
        odds = 0
        g = defaultdict(lambda: { 'list': [], 'odd': 0 })
        for i in range(len(graphs)):
            g[find(i)]['list'].append(nums[i])
            g[find(i)]['odd'] += i & 1

        
        for graph in g.values():
            graph['list'].sort()
            odds += sum(graph['list'][:graph['odd']])
            evens += sum(graph['list'][graph['odd']:])

        return evens - odds

        
