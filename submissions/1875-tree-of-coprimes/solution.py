class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        ret = [-1] * len(nums) 
        def dfs(opts, parent, curr, depth):
            d = -1
            for v, (i, dd) in opts.items():
                if i < 0:
                    continue
                if gcd(v, nums[curr]) == 1:
                    if dd > d:
                        d = dd
                        ret[curr] = i
            
            prev, prev_d = opts[nums[curr]]
            opts[nums[curr]] = (curr, depth)
            for i in graph[curr]:
                if i == parent:
                    continue
                dfs(opts, curr, i, depth + 1)

            opts[nums[curr]] = (prev, prev_d)

        
        dfs(defaultdict(lambda: (-1, -1)), -1, 0, 0)
        return ret


        
